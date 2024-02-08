import os
import requests
from dotenv import load_dotenv

load_dotenv()

account = os.getenv("OKDESK_ACCOUNT_NAME")
okdesk_api_token = os.getenv("OKDESK_API_TOKEN")


def get_okdesk_user_email_by_id(user_id: str) -> str:
    response = requests.get(f'https://{account}.okdesk.ru/api/v1/contacts/?api_token={okdesk_api_token}&id={user_id}')
    return response.json().get("email")





