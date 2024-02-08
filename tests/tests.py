from fastapi import requests
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from bitrix_bot.bitrix_bot import get_user_id_bitrix, send_rate_request
from tests.webhook_example import webhook_request
from utils import get_okdesk_user_email_by_id


def test(client: TestClient, db: Session):
    response = client.post("http://localhost:8000/api/v1/okdesk/create_rate_request", json=webhook_request)

    get_okdesk_user_email_by_id(db.get)


    user_id = get_user_id_bitrix('eldoradozolotoe1@gmail.com')
    print(user_id)

    result = send_rate_request('eldoradozolotoe1@gmail.com')
    print(result)
