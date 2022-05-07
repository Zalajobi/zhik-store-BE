import smtplib
import os


def sendmail(message):
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    # smtp_server.starttls()
    smtp_server.login('zhikrullah.ranti@gmail.com', 'nqisvjygyhtspqvh')
    # smtp_server.login(email, password)
    smtp_server.send_message(message)
