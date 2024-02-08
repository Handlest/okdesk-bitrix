import datetime
import os
import requests
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from config import get_db
from models.request_model import RatingRequest
from utils import get_okdesk_user_email_by_id


okdesk_router = APIRouter(prefix="/api/v1/okdesk", tags=["okdesk"])

load_dotenv()
account = os.getenv("OKDESK_ACCOUNT_NAME")
okdesk_api_token = os.getenv("OKDESK_API_TOKEN")


@okdesk_router.post(path="/create_rate_request")
def create_request(payload: dict = Body(...), db: Session = Depends(get_db)):
    """Функция, принимающая запросы с вебхука Okdesk при любом обновлении статуса заявки"""
    code_status = payload.get("event").get("new_status").get("code")
    if code_status == "closed":
        client_author_id = payload.get("issue").get("contact").get("id")
        issue_id = payload.get("issue").get("id")
        author_email = get_okdesk_user_email_by_id(client_author_id)
        new_rating_request = RatingRequest(email=author_email, author_id=client_author_id,
                                           issue_id=issue_id, closed_at=datetime.date.today())
        db.add(new_rating_request)
        db.commit()
        return {'message': 'Rating request added successfully'}
    return {"message": f"code_status was changed to: {code_status}. Skipping"}


@okdesk_router.post(path="/change_rate/{rate}&{user_email}")
def change_status(rate: str, user_email: str, db: Session = Depends(get_db)):
    """Функция, получающая от бота ответ пользователя и устанавливающая оценку в соответствующую заявку Okdesk"""
    db_object: RatingRequest = db.query(RatingRequest).filter(RatingRequest.email == user_email).first()
    issue_id = db_object.issue_id
    response = requests.post(f"https://{account}.okdesk.ru/api/v1/issues/{issue_id}/rates?api_token={okdesk_api_token}",
                             json={'issue': {"rate": rate}})
    if response.status_code == 200:
        db.delete(db_object)
        db.commit()
        return {'message': f'Request with id {issue_id} was rated as {rate}'}
    raise HTTPException(status_code=response.status_code, detail=response.json())
