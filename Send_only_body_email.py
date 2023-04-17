from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(sender,app_password,receiver, message):
    try:
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(sender, app_password)

  

        # sending the mail
        s.sendmail(sender, receiver, message)
        print("Email Send")
        # terminating the session
        s.quit()
    except Exception as e:
        print(e)
        return False
    return True


send_mail(sender,app_password,receiver, message)
