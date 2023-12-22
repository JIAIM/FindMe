import smtplib


def send_email(message, email):
    sender = 'romanin@sliceum.com'
    password = 'ivtn eclr lwmp nkef'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender, password)
        server.sendmail(sender, email, message)

        print(message)
    except Exception as _ex:
        print(_ex)
