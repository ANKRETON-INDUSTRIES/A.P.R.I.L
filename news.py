import speech_recognition as sr
import pyttsx3
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')





voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)



def speak(audio):
    print('APRIL: ' + audio)
    engine.say(audio)
    engine.runAndWait()




news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  speak(news.title.text)
  print("-"*12)
 
