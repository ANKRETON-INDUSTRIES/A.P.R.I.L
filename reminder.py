import datetime
import pyttsx3
import speech_recognition as sr
import win10toast
from playsound import playsound
engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def myCommand():
   
    r = sr.Recognizer()

    
    with sr.Microphone() as source:                                                                      

        audio = r.listen(source)
        query=''
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
       
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
###########################################################
def myCommand2():
   
    r = sr.Recognizer()

    
    with sr.Microphone() as source:                                                                      

        audio = r.listen(source)
        query2=''
    try:
        query2 = r.recognize_google(audio, language='en-in')
        print('User: ' + query2 + '\n')
       
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query2 = str(input('Command: '))

    return query2

###############################################################
def myCommand3():
   
    r = sr.Recognizer()

    
    with sr.Microphone() as source:                                                                      

        audio = r.listen(source)
        query3=''
    try:
        query3 = r.recognize_google(audio, language='en-in')
        print('User: ' + query3 + '\n')
       
    except sr.UnknownValueError:
        speak('am or pm')
        query3 = str(input('Command: '))

    return query3
##################################################################
def myCommand4():
   
    r = sr.Recognizer()

    
    with sr.Microphone() as source:                                                                      

        audio = r.listen(source)
        query4=''
    try:
        query4 = r.recognize_google(audio, language='en-in')
        print('User: ' + query4 + '\n')
       
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the words!')
        query4 = str(input('what want to tell: '))

    return query4

###############################################################
def speak(audio):
    print('APRIL: ' + audio)
    engine.say(audio)
    engine.runAndWait()



    
speak("welcome to,, reminder")
#########
speak("hour to remind")
query=myCommand()

#########
speak("minute to remind")
query2=myCommand2()

#########
speak("am or pm boss")
query3=myCommand3()
#########
speak("what want to tell in reminder")
query4=myCommand4()



if (str(query3) == "pm"):
    
  query=int(query) + 12
speak("reminder set boss")

while(1==1):
    if(int(query) ==datetime.datetime.now().hour and
       int(query2)==datetime.datetime.now().minute):
        
        print("reminder on")
        reminder=win10toast.ToastNotifier()
        reminder.show_toast('A.P.R.I.L',query4,duration=20)
        playsound('cock.aac')

        break
print("exited")



