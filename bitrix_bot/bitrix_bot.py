import os
from dotenv import load_dotenv
import fast_bitrix24

load_dotenv()
server_link = os.getenv("SERVER_URL")
account = os.getenv("BITRIX_ACCOUNT_NAME")
get_id_key = os.getenv("BITRIX_GET_ID_KEY")
send_message_key = os.getenv("BITRIX_SEND_MESSAGE_KEY")


# ToDo: Подобрать цвета потемнее для кнопок
def send_rating_request(user_email: str, issue_id: str):
    """
    Отправляет пользователю в битрикс сообщение с просьбой оценить уровень обслуживания по заявке с возможностью
    выбора одного из трёх вариантов оценки
    """
    b = fast_bitrix24.Bitrix(f'https://{account}.bitrix24.ru/rest/1/{send_message_key}')
    dialog_id = get_user_id_bitrix(user_email)
    message = "Пожалуйста, оцените уровень обслуживания по заявке"
    keyboard = [
        {"TEXT": "Отлично", "LINK": f"{server_link}/api/v1/okdesk/change_rate?rate=good&&issue_id={issue_id}",
         "BG_COLOR": "#7CFC00", "TEXT_COLOR": "#fff", "DISPLAY": "LINE", },
        {"TEXT": "Хорошо", "LINK": f"{server_link}/api/v1/okdesk/change_rate?rate=normal&&issue_id={issue_id}",
         "BG_COLOR": "#FFD700", "TEXT_COLOR": "#fff", "DISPLAY": "LINE", },
        {"TEXT": "Плохо", "LINK": f"{server_link}/api/v1/okdesk/change_rate?rate=bad&&issue_id={issue_id}",
         "BG_COLOR": "#DC143C", "TEXT_COLOR": "#fff", "DISPLAY": "LINE", }]
    response = b.call(f'im.message.add', items={'DIALOG_ID': dialog_id, 'MESSAGE': message, "KEYBOARD": keyboard})
    return response


def get_user_id_bitrix(user_email: str) -> str:
    """Получает id пользователя в системе bitrix по его email"""
    b = fast_bitrix24.Bitrix(f'https://{account}.bitrix24.ru/rest/1/{get_id_key}')
    response = b.get_all("user.search", params={'email': user_email}).cr_await
    users_found_count = len(response)
    if users_found_count > 1:
        raise Exception(f"Found more than one user with email {user_email}")
    elif users_found_count == 0:
        raise Exception(f"User with email {user_email} not found")
    return response[0].get("ID")
