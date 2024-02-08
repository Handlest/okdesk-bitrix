webhook_request = {
  "event": {
    "event_type": "new_ticket_status",
    "author": {
      "first_name": "Иван",
      "last_name": "Иванов",
      "patronymic": "Иванович",
      "id": "1",
      "type": "employee"
    },
    "old_status": {
      "code": "opened",
      "name": "Открыта"
    },
    "new_status": {
      "code": "completed",
      "name": "Решена"
    },
    "comment": {
      "id": "5880",
      "is_public": True,
      "content": "Работы проверены"
    },
    "attachments": [
      {
        "id": "519",
        "is_public": True,
        "attachment_file_name": "Screenshot(1).png",
        "description": "Документ №1",
        "attachment_file_size": "23460",
        "created_at": "2021-04-14T16:58:03.921+03:00"
      }
    ],
    "parameters": [
      {
        "code": "address",
        "name": "Адрес вызова",
        "type": "ftstring",
        "value": "ул. Ленина 44"
      }
    ],
    "time_entries": {
      "id": "13",
      "comment": "Проверка товара",
      "spent_time": "2",
      "employee": {
        "first_name": "Иван",
        "last_name": "Иванов",
        "patronymic": "Иванович",
        "id": "1"
      }
    },
    "old_assignee": {
      "group": {
        "name": "Отдел контроля качества",
        "id": "2"
      },
      "employee": {
        "first_name": "Пётр",
        "last_name": "Петрович",
        "patronymic": "Петров",
        "id": "6"
      }
    },
    "new_assignee": {
      "group": {
        "name": "Отдел продаж",
        "id": "2"
      },
      "employee": {
        "first_name": "Аглая",
        "last_name": "Ивановна",
        "patronymic": "Епанчина",
        "id": "5"
      }
    }
  },
  "issue": {
  "title": "Требуется мастер на выезд",
  "planned_execution_in_hours": "12.5",
  "id": "153",
  "parent_id": None,
  "child_ids": [
    93,
    94,
    91
  ],
  "description": "Обнаружена неисправность на объекте",
  "type": {
    "code": "service",
    "name": "Обслуживание",
    "inner": False
  },
  "priority": {
    "code": "low",
    "name": "Низкий"
  },
  "status": {
    "code": "opened",
    "name": "Открыта"
  },
  "old_status": {
    "code": "completed",
    "name": "Решена"
  },
  "rate": "normal",
  "client": {
    "company": {
      "name": "ООО Транспортное обслуживание",
      "id": "15"
    },
    "contact": {
      "first_name": "Николай",
      "last_name": "Ставрогин",
      "patronymic": "Всеволодович",
      "id": "21"
    }
  },
  "agreement": {
    "id": "34",
    "title": "Договор технического обслуживания №2016-03/1"
  },
  "maintenance_entity": {
    "name": "053 Камаз Т1",
    "id": "43",
    "address": {
      "string_value": "Екатеринбург, Свердловская область, 620141, Россия",
      "coordinates": [
        56.866532,
        60.596592
      ]
    }
  },
  "equipments": [
    {
      "serial_number": "123N3",
      "inventory_number": "453S-A",
      "id": "96",
      "type": {
        "code": "laptop",
        "name": "Ноутбук"
      },
      "manufacturer": {
        "code": "asus",
        "name": "Asus"
      },
      "model": {
        "code": "x50sm",
        "name": "x50sm"
      }
    }
  ],
  "author": {
    "first_name": "Андрей",
    "last_name": "Елизаров",
    "patronymic": "Валерьевич",
    "id": "44",
    "type": "employee"
  },
  "assignee": {
    "group": {
      "name": "Тех. обслуживание",
      "id": "1"
    },
    "employee": {
      "first_name": "Иван",
      "last_name": "Петров",
      "patronymic": "Сергеевич",
      "id": "116"
    }
  },
  "coexecutors": [
    {
      "group": {
        "name": "Тех. обслуживание",
        "id": "1"
      },
      "employee": {
        "first_name": "Иван",
        "last_name": "Петров",
        "patronymic": "Сергеевич",
        "id": "116"
      }
    }
  ],
  "observers": {
    "employees": [
      {
        "first_name": "Петр",
        "last_name": "Антонов",
        "patronymic": "Захарович",
        "id": "113"
      }
    ],
    "contacts": [
      {
        "first_name": "Артем",
        "last_name": "Акмаев",
        "patronymic": "Викторович",
        "id": "121"
      }
    ],
    "groups": [
      {
        "name": "Отдел диагостики",
        "id": "1"
      }
    ]
  },
  "created_at": "2016-09-30T09:28:50.499+03:00",
  "deadline_at": "2016-09-30T17:28:50.000+03:00",
  "planned_reaction_at": "2016-10-22T13:00:00.000+03:00",
  "start_execution_until": "2019-09-01T00:00:00.000+03:00",
  "completed_at": None,
  "reacted_at": "2016-10-15T15:31:14.383+03:00",
  "parameters": [
    {
      "code": "address",
      "name": "Адрес вызова",
      "type": "ftstring",
      "value": "ул. Ленина 44"
    }
  ],
  "attachments": [
    {
      "id": "8",
      "attachment_file_name": "photo.jpg",
      "description": "Фотография неисправности",
      "attachment_file_size": "4149",
      "is_public": False,
      "created_at": "2016-09-30T09:28:50.499+03:00"
    }
  ]
}
}