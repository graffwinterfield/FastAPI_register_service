from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config import settings


class Mail:
    @staticmethod
    def check_conn(server):
        try:
            status = server.noop()[0]
            print(status)
        except Exception as e:
            print(e)
            status = -1
        return True if status == 250 else False

    @staticmethod
    def connect_to_mail():
        password = settings.SMTP_PASSWORD
        email_from = settings.SMTP_LOGIN
        smtp_host = settings.SMTP_HOST
        smtp_port = settings.SMTP_PORT
        try:
            server = smtplib.SMTP(f'{smtp_host}: {smtp_port}')
            server.ehlo()
            server.starttls()
            server.login(email_from, password)
            return server
        except smtplib.SMTPServerDisconnected:
            return 'Error disconnect'
        except Exception as e:
            print(f"Error connecting to SMTP server: {e}")

    @staticmethod
    def send_email(server, text):
        msg = MIMEMultipart()
        msg['From'] = settings.SMTP_EMAIL
        msg['To'] = settings.EMAIL
        msg['Subject'] = 'API_service'
        msg.attach(MIMEText(text, 'plain'))
        server.send_message(msg)
        return server


def save_to_db(data, db):
    db.add(data)
    db.commit()
    db.refresh(data)
