import os
import datetime
import win10toast
from playsound import playsound
toaster = win10toast.ToastNotifier()
notify = str(input("wht is the message you want to remember"))
alarmH = int(input("What hour do you want the alarm to ring? "))
alarmM = int(input("What minute do you want the alarm to ring? "))
amPm = str(input("am or pm? "))
os. system('clear')
print("Waiting for the time push the reminder at",alarmH,alarmM,amPm)
if (amPm == "pm"):
        alarmH = alarmH + 12
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute):
        print(notify
        )
        playsound ("F:\cock.wav")
        toaster.show_toast('APRIL',  notify , icon_path='F:\wp3850825_4k_pc_wallpapers_uG3_icon.ico', duration=30)
        break
