# Отправить письмо через Django + Gmail

## Настройка 

- В файле `email_back/settings.py` поменяйте следующие строчки:

###### `email_back/settings.py`
```py
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'Ваш gmail')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'Ваш app password, если используете gmail')
```

- В файле `send_email/views.py` поменяйте следующие строчки:

###### `send_email/views.py`
```py
email = EmailMessage(
        'Заголовок письма',
        'Тело письма',
        'Кто отправляет',
        ['Кому отправляет'],
    )
```

## Запуск

- Чтобы запустить Django сервер используйте:

```powershell
python manage.py runserver
```

- Затем перейдите на [http://127.0.0.1:8000/send-email/](http://127.0.0.1:8000/send-email/), чтобы письмо отправилось.