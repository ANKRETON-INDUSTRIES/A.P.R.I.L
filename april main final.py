import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import wmi
import requests
import re
import subprocess
import time

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('XEG2HJ-XJ43W7RLL3')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)



def speak(audio):
    print('APRIL: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()





speak('Your password please:')
num=eval(input("Enter the password:"))
if(num==12345):
    speak('okay , Boss')
else:
    speak('ACCESS DENIED')
    speak('april in alert mode, system deactivated')
    sys.exit()


os.startfile('E:\\video april.py')


speak('Hi BOSS ')
speak('hello from ankreton industries')
speak('this is april online and welcome to the digital advanced workspace of mine')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:
        query = myCommand()
        query = query.lower()



        if  'good morning' in query:
            speak('Good morning Boss')

        elif 'good evening' in query:
            speak('Good evening Boss')

        elif 'corona update' in query:
            speak('redirecting to page')
            webbrowser.open('https://www.mygov.in/covid-19')

        elif 'who created you' in query:
            speak(' I WAS CREATED BY THE GROUP ANKRETON INDUSTRIES')
            speak('ANKRETON INDUSTRIES IS A GROUP OF STUDENTS ALL AROUND KERALA')
            speak('THIS GROUP MAKES MANY AWESOME PROJECTS FOR THE FUTURE')

        elif 'open calculator' in query:
            speak('opening calculator boss')
            calc="E:\\calc.py"
            os.startfile(calc)


        elif 'who are you' in query:
            os.startfile('E:\\qqqqqqqqqqqqqqq.py')
            time.sleep(92)

        elif 'hotel bill' in query:
            os.startfile('E:\\restaurant.py')

        elif 'portal' in query:
            os.startfile('E:\\gauthu.py')

        elif 'news for today' in query:
           os.startfile('E:\\news.py')
           time. sleep(30)


        elif 'play game' in query:
            speak('ok boss i have 6 games to play')
            speak('pokemon 1 path 2 mines 3 hvideoangman 4 pacman 5 puzzle 6')
            print('pokemon 1 path 2 mines 3 hangman 4 pacman 5 puzzle 6')
            num=eval(input('enter the number of game neede'))
            if num == 1:
                speak('welcome to pokemon')
                speak('in this you will battle with charlizard and bulbasoures')
                speak('this is a stratergy game')
                game='E:\\pokemon.py'
                os.startfile(game)

            elif num == 2:
                speak('this is between you and me')
                speak('enter the coordinate of first and last point')
                speak('draw as many obstacles you want i will find the path')
                speak('press spacebar after drawing the obstacles')
                game='E:\\path_finding.py'
                os.startfile(game)

            elif num ==3:
                speak('welcome to the world of classic mines')
                os.startfile('E:\\mines.py')

            elif num ==4:
                speak('guess the word otherwise you will be a dead man ha ha ha')
                os.startfile('E:\\hangman.py')

            elif num ==5:
                speak('welcome to the classic game of pacman')
                os.startfile('E:\\pacman.py')

            elif num==6:
                os.startfile('E:\\puzzle.py')

        elif 'play pokemon' in query:
            speak('welcome to pokemon')
            speak('in this you will battle with charlizard and bulbasoures')
            os.startfile('E:\\pokemon.py')

        elif 'play path' in query:
            speak('this is between user you and me')
            speak('enter the coordinate of first and last point')
            speak('draw as many obstacles you want i will find the path')
            speak('press spacebar after drawing the obstacles')
            os.startfile('E:\\path_finding.py')

        elif 'play mines' in query:
            speak('welcome to the world of classic mines')
            os.startfile('E:\\mines.py')

        elif 'play hangman' in query:
            speak('guess the word otherwise you will be a dead man ha ha ha')
            os.startfile('E:\\hangman.py')

        elif 'play puzzle' in query:
            speak('lets see who has the brain')
            speak('this is a memory test and a puzzle')
            speak('i bet you cant win')
            os.startfile('E:\\puzzle.py')

        elif 'take video' in query:
            speak('opening april video suit boss')
            os.startfile('E:\\april video.py')

        elif 'play pacman' in query:
            speak('welcome to the classic game of pacman')
            os.startfile('E:\\pacman.py')

        elif 'paint' in query:
            webbrowser.open('https://canvaspaint.org/#local:ca752fd102ff2')

        elif 'photo editor' in query:
            webbrowser.open('https://www.photopea.com')

        elif 'video editor' in query:
            webbrowser.open('https://moviemakeronline.com')


        elif 'good afternoon' in query:
            speak('Good afternoon Boss')

        elif 'set an alarm' in query:
            os.startfile('E:\\alarm.py')

        elif 'remind me ' in query:
            os.startfile('E:\\test reminder.py')



        elif 'play music' in query:
            music_dir = 'E:\\april music.mp3'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0] ))

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'shutdown' in query:
              speak('warning you are about to shutdown your sysytem')
              speak('to safely proceed to shutdown say yes')
              if 'yes' in query:
                  speak('your are about to abort the system within 10 seconds')
                  os.system("shutdown  /s  /t 10")
              else:
                  speak('sorry sir i could not execute the command')
                  pass



        elif 'restart' in query:
            speak('you are about to restart the system')
            speak('to safely proceed to restart say yes')
            if 'yes' in query:
                speak('boss younare about to restart the system')
                os.system("restart /r /t 10")
            else:
                speak('sorry sir i could not execute the command')
                pass


        elif 'can i change your voice' in query:
            speak('Just a second Boss!...')
            speak('yes i have a brother')
            speak('calling my brother')


            voices = engine.getProperty('voices')

            engine.setProperty('voice', voices[len(voices)-2].id)


            speak('Hello boss')
            speak('welcome to my digital, advanced ,workspace')
            speak('I AM ANKRETON ONLINE')




        elif 'open' in query:
                  reg_ex = re.search('open (.+)', query)
                  if reg_ex:
                      domain = reg_ex.group(1)
                      url = 'https://www.' + domain
                      webbrowser.open(url)
                      speak('The website you have requested has been opened for you Sir.')
                  else:
                          speak('Sorry sir i cannot connect at the moment')




        elif 'tell me a joke' in query:
         res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"applicationvideo/json"}
                )
         if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
         else:
            speak('oops!I ran out of jokes')



        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'April' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("parthiv.kp28@gmail.com", '9142000914@arjun.k')
                    server.sendmail('parthiv.kp28@gmail.com', "aashikhello@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! the server is down at the moment!')


        elif 'quit' in query or 'exit' in query or 'stop'  in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()


        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()



        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('got it, boss ')
                    speak('APRIL SAYS')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=5)
                    speak('Got it.')
                    speak('APRIL    says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')
