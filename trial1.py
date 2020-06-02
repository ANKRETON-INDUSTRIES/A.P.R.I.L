import requests
import urllib.request
from bs4 import BeautifulSoup
import smtplib


web=eval(input("enter the website url you want to remember in single qoutes"))

URL=web

headers={"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

def check_price():
    
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[2:6])
    print(converted_price)

    if(converted_price<50000):
        print("price has fallen")
    else:
        print("waiting")

check_price()
