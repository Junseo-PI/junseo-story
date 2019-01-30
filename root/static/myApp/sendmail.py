from django.core.mail import EmailMessage

email = EmailMessage('', '', to=['jssolomon@naver.com'])

email.send()
