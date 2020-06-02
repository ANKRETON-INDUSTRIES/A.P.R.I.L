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



engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('XEG2HJ-XJ43W7RLL3')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)



def speak(audio):
    print('Computer: ' + audio)
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

os.startfile('E:\\video april.py')



speak('Your password please:')
num=eval(input("Enter the password:"))
if(num==12345):
    speak('okay , Boss')
else:
    speak('ACCESS DENIED')
    speak('april in alert mode, system deactivatind')
    sys.exit()    

speak('Hi BOSS ')
speak('I am your digital assistant  APRIL!')
speak('How may I help you?')


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
       
        if 'open youtube' in query:
            speak('okay , Boss')
            webbrowser.open('www.youtube.com')        

        elif 'open google' in query:
            speak('okay , Boss')
            webbrowser.open('www.google.co.in')

        elif 'good morning' in query:
            speak('Good morning Boss')

        elif 'good evening' in query:
            speak('Good evening Boss')

        elif 'corona updates' in query:
            speak('redirecting to page')
            webbrowser.open('https://www.mygov.in/covid-19')

        elif 'open calculator' in query:
            speak('opening calculator boss')
            calc="E:\\calc.py"
            os.startfile(calc)


        elif 'joke' in query:
         res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
         if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
         else:
            speak('oops!I ran out of jokes')

  


        elif 'play game' in query:
            speak('ok boss i have 2 games to play')
            print('for pokemon 1 and path finding 2')
            num=eval(input('enter the number of game neede'))
            if num == 1:
                game='E:\\pokemon.py'
                os.startfile(game)

            elif num == 2:
                game='E:\\path_finding.py'
                os.startfile(game)

        elif 'paint' in query:
            speak('opening paint boss')
            os.startfile('E:\Python-Drawing-Program-master\main.py')
            
           
     
        elif 'good afternoon' in query:
            speak('Good afternoon Boss')

        elif 'play music' in query:
            music_dir = 'F:\\file_example_MP3_2MG.mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")      

        elif 'programmer' in query:
            speak('Just a second Boss!...')
            speak('Establishing Secure Connection')
            speak('Done')
           

            voices = engine.getProperty('voices')
            
            engine.setProperty('voice', voices[len(voices)-2].id)
                 
               
            speak('Hello boss')
            speak('I am ,programmer ,')
            speak('welcome to my digital, advanced ,workspace')

        elif 'open notepad' in query:
            speak('Opening notepad boss..')
            os.system('Notepad.exe')    
           
        elif 'open gmail' in query:
            speak(',okay , Boss')
            webbrowser.open('www.gmail.com')

        elif 'calculator code' in query:
            speak('yes boss')
            code='E:\\calc.txt'
            os.startfile(code)

        elif 'code to check divisibility' in query:
            speak('yes boss')
            data='E:\\data.txt'
            os.startfile(data)

        elif 'open chrome' in query:
            speak('Opening chrome boss..')
            os.system('Google Chrome.exe')    

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
       
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
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
                    speak('Predator    says -')
                    speak(results)
                   
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA      says - ')
                    speak(results)
       
            except:
                webbrowser.open('www.google.com')
       
        speak('Next Command! Sir!')
      
