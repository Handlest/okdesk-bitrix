from datetime import datetime, timedelta
from typing import List

from sqlalchemy.orm import Session
from config import SessionLocal
from models.request_model import RatingRequest
from routers.okdesk_routes import change_status


def clear_old_requests(db: Session = SessionLocal()):
    """
    Задача для cron. Каждый час собирает заявки, на которые не поступил ответ за последние 24 часа
    и проставляет им оценку отлично
    """
    twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
    requests_to_rate: List[RatingRequest] = (db.query(RatingRequest)
                                             .where(RatingRequest.closed_at <= twenty_four_hours_ago).all())
    for request in requests_to_rate:
        change_status(rate='good', issue_id=request.issue_id)
        db.delete(request)
    db.commit()
    db.close()


clear_old_requests()
