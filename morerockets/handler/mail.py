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


def sendOnAllMails(subj, msg_text, rec):
    for r in rec:
        msg_text += f"<p>To unsubscribe use the <a href=\"http://morerocket.us-east-1.elasticbeanstalk.com/api/unsubscribe?email={r}\">link</a></p>"
        msg = Message(subject=subj,html=msg_text,
                    sender="nasamorerockets@gmail.com",
                    recipients=[r])
        mail.send(msg)
    return "Sent"
