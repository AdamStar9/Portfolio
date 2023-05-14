import smtplib, ssl
import os

password = os.environ["PASSWORD"]


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "adam.starostik9@gmail.com"
    receiver = "adam.starostik9@gmail.com"
    context = ssl.create_default_context()
    print(password)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


print(password)





