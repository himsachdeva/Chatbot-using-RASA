from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_USE_TLS": False,  # Transport Layer Security
    "MAIL_USE_SSL": True,  # Secure Sockets Layer
    "MAIL_PORT": 465,  # For using SSL
    "MAIL_USERNAME": 'random.upgrad@gmail.com',
    "MAIL_PASSWORD": 'P@$$w0rd15'
}
app.config.update(mail_settings)
mail = Mail(app)


def send_mail(emailid, html_msg):
    with app.app_context():
        msg = Message(sender=app.config.get("MAIL_USERNAME"), recipients=[emailid])
        msg.subject = "Foodie search results"
        msg.html = html_msg
        mail.send(msg)
