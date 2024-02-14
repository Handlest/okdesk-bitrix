# Инициализация проекта
1. Клонируем репозиторий на сервер 
```
git clone https://github.com/Handlest/okdesk-bitrix
```

2. Создаём виртуальное окружение и устанавливаем необходимые зависимости
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Копируем содержимое файла example.env в новый файл .env и настраиваем его под себя

3. Запускаем контейнер с базой данных и fastAPI 
```
docker-compose -f docker-compose.yaml up --remove-orphans --force-recreate --build
```

4. Создаём cron для автоматического оценивания заявок оставленных без ответа

```
crontab -e
0 * * * * cd /путь/до/папки/проекта && venv/bin/python cron_task.py
```

# Пояснение к настройке вебхуков

### Okdesk
1. Создаём вебхук на событие "изменение статуса заявки".  
2. В вызываемом URL указываем `*адрес_сервера*/api/v1/okdesk/create_rate_request`
3. В переменную `OKDESK_ACCOUNT_NAME` передаём имя аккаунта okdesk
4. В переменную `OKDESK_API_TOKEN` токен для вебхука

### Bitrix24
1. Создаём входящий вебхук на метод user.search   
2. Добавляем права: `user`, `user_brief`, `user_basic`, `user.userfield`   
3. Копируем только токен из адреса вида `https://{Пользователь}.bitrix24.ru/rest/1/{Токен} `  
4. Токен добавляем в .env файл в переменную `BITRIX_GET_ID_KEY`   


1. Создаём входящий вебхук на метод `imbot.message.add  `  
2. Добавляем права: `im`, `imbot`    
3. Копируем только токен из адреса вида `https://{Пользователь}.bitrix24.ru/rest/1/{Токен} `
4. Токен добавляем в .env файл в переменную `BITRIX_SEND_MESSAGE_KEY`

# Пайплан работы программы
```mermaid
graph TB
change_status[Смена статуса заявки \n в okdesk на закрыто]
request_db(Добавление информации \nо заявке в бд)
request_bitrix(Отправка запроса на\n оценку пользователю в bitrix)
if_answer[Получение ответа пользователя]
else_not_answer[Истекло 24 часа с\n момента закрытия заявки]
save_answer(Отправка информации об оценке в Okdesk)
delete_db(Удаление информации \nо заявке из бд)

util_get_email([Получаем email в okdesk\n по id из заявки])
util_get_id_by_email([Получаем id в\n bitrix по email])


change_status --> request_bitrix
change_status --> util_get_email
util_get_email --> util_get_id_by_email
util_get_email --> request_db
util_get_id_by_email --> request_bitrix

request_bitrix --> if_answer
request_bitrix -->else_not_answer

if_answer --> save_answer
else_not_answer --> save_answer

save_answer --> delete_db
```
