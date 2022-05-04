import smtplib
import datetime as dt
from random import choice


def sundays_emails():
    # Usando o arquivo .txt das citações
    with open("quotes.txt", "r") as citacoes:
        quote_list = citacoes.readlines()

    # Informações necessárias para o envio do email
    host = "host do seu e-mail"
    port = int
    MY_EMAIL = "seu email"
    MY_PASSWORD = "senha do seu email"
    target_email = "email que receberá a msg"


    # Iniciando o servidor
    with smtplib.SMTP(host, port) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=target_email,
            msg=f"Subject:Mensagem Motivacional da Segunda-feira :D!\n\n{choice(quote_list)}"
        )


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    sundays_emails()

sundays_emails()
