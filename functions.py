from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config import settings


class Mail:
    def connect_to_mail_and_send_email(self):
        password = settings.SMTP_PASSWORD
        email_from = settings.SMTP_LOGIN
        print(password, email_from)
        smtp_host = settings.SMTP_HOST
        smtp_port = settings.SMTP_PORT
        server = smtplib.SMTP(f'{smtp_host}: {smtp_port}')
        server.ehlo()
        server.starttls()
        server.login(email_from, password)

        return server

    def send_email(self, server, text):
        msg = MIMEMultipart()  # Создаем сообщение
        msg['From'] = settings.SMTP_EMAIL  # Адресат
        msg['To'] = settings.EMAIL  # Получатель
        msg['Subject'] = 'Тема сообщения'  # Тема сообщения
        msg.attach(MIMEText(text, 'plain'))  # Добавляем в сообщение текст
        server.send_message(msg)
        return server

def save_to_db(data, db):
    db.add(data)
    db.commit()
    db.refresh(data)
