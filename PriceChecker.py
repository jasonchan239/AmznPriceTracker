import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/Razer-DeathAdder-Lighting-Programmable-Rubberized/dp/B082G5SPR5/ref=sr_1_3?crid=24WNN29TG8UNT&dchild=1&keywords=deathadder+v2&qid=1595871622&sprefix=deathadd%2Caps%2C157&sr=8-3'

headers  = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'lxml')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    new_price=float(price[5:])

    if(new_price<80.00):
        send_mail()

    print(title.strip())
    print(new_price);

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    #Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to
    #identify itself when connecting to another email server to start the process of sending an email
    server.starttls()
    server.ehlo()

    server.login('***@gmail.com','***')

    subject='Price has fallen!'
    body = 'check:https://www.amazon.ca/Razer-DeathAdder-Lighting-Programmable-Rubberized/dp/B082G5SPR5/ref=sr_1_3?crid=24WNN29TG8UNT&dchild=1&keywords=deathadder+v2&qid=1595871622&sprefix=deathadd%2Caps%2C157&sr=8-3'
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail(
        '***@gmail.com',
        '***@gmail.com',
        msg
    )
    print("email has been sent")
    server.quit()

check_price()
