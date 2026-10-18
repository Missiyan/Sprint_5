Sprint_5 UI-автотесты
для учебного сервиса «Доска» https://qa-desk.education-services.ru

структура:

Sprint_5/
├── tests/ #сценарии
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_logout.py
│   └── test_advertisement.py   
├── conftest.py    # фикстуры
├── locators.py                   
├── config.py                     
├── utils.py   # генерация email, password, доп функции
├── requirements.txt
├── README.md
└── .gitignore

В config.py задать:

BASE_URL = "https://qa-desk.education-services.ru"
EXISTING_USER_EMAIL = "..."       # заранее зарегистрированный пользователь
EXISTING_USER_PASSWORD = "..."