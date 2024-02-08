import os
from dotenv import load_dotenv
import fast_bitrix24

load_dotenv()
server_link = os.getenv("SERVER_URL")


# ToDo: Подобрать цвета потемнее для кнопок

def send_rate_request(user_email: str):
    b = fast_bitrix24.Bitrix('https://b24-8jd96p.bitrix24.ru/rest/1/ju70h1fv6buq18ju')
    dialog_id = get_user_id_bitrix(user_email)
    message = "Пожалуйста, оцените уровень обслуживания по заявке"
    keyboard = [
        {"TEXT": "Отлично", "LINK": f"{server_link}?rate=good&user_email={user_email}", "BG_COLOR": "#7CFC00",
         "TEXT_COLOR": "#fff", "DISPLAY": "LINE", },
        {"TEXT": "Хорошо", "LINK": f"{server_link}?rate=normal&user_email={user_email}", "BG_COLOR": "#FFD700",
         "TEXT_COLOR": "#fff", "DISPLAY": "LINE", },
        {"TEXT": "Плохо", "LINK": f"{server_link}?rate=bad&user_email={user_email}", "BG_COLOR": "#DC143C",
         "TEXT_COLOR": "#fff", "DISPLAY": "LINE", }]
    response = b.call(f'im.message.add', items={'DIALOG_ID': dialog_id, 'MESSAGE': message, "KEYBOARD": keyboard})
    return response


# ToDo: Переписать на асинхронный, чтобы избавиться от подсветки корутин
def get_user_id_bitrix(user_email: str) -> str:
    b = fast_bitrix24.Bitrix('https://b24-8jd96p.bitrix24.ru/rest/1/e5szb22tag1dxb0j')
    response = b.get_all("user.search", params={'email': user_email})
    users_found_count = len(response)
    if users_found_count > 1:
        raise Exception(f"Found more than one user with email {user_email}")
    elif users_found_count == 0:
        raise Exception(f"User with email {user_email} not found")
    return response[0].get("ID")


send_rate_request('eldoradozolotoe1@gmail.com')