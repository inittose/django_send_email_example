from django.core.mail import EmailMessage
from django.http import HttpResponse

def send_notification():
    email = EmailMessage(
        'Заголовок письма',
        'Тело письма',
        'Кто отправляет',
        ['Кому отправляет'],
    )
    email.send(fail_silently=False)

def send_email_view(request):
    send_notification()  # Вызов функции отправки письма
    return HttpResponse('Письмо отправлено!')