import requests
import urllib.request
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/FX705DT-AU092T-Graphics-5-3550H-Windows-Stealth/dp/B07WLQS4F7/ref=sr_1_4?crid=17O6GY892LFL6&dchild=1&keywords=asus+tuf+gaming+fx505dt&qid=1590089925&sprefix=asus+tuf%2Caps%2C542&sr=8-4&tag=coa_in-21'

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
