from flask_mail import Mail, Message
from morerockets import app

app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='nasamorerockets@gmail.com',
    MAIL_PASSWORD='More_Rockets2018',
))

mail = Mail(app)


def sendOnAllMails(subj, msg, rec):
    msg = Message(subject=subj,body=msg,
                  sender="nasamorerockets@gmail.com",
                  recipients=rec)
    mail.send(msg)
    return "Sent"
