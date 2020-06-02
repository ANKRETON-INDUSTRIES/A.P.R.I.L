import sys
import random
from time import ctime
import speech_recognition as sr
import webbrowser
import wikipedia 
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
from gtts import gTTS
import pygame

def action():
    print(myline.text())
    x=myline.text()
    try:
        url='https://google.com/search?q=' + x
        webbrowser.get().open(url)
        w="user here is what i found for "+x
        l1.setText(w)
        
    except:
        print("sorry i did not got it")
def action2():
    print(myline2.text())
    y=myline2.text()
    try:
        l1.setText("the answer is: "+(wikipedia.summary(y,sentences=2)))
    except:
        z="sorry"
        l1.setText(z)



app=QApplication(sys.argv)
win=QMainWindow()
win.setFixedSize(800,450)
win.setWindowTitle("evie assistant your partner")


label3 = QtWidgets.QLabel(win)
label3.setText("")
label3.setGeometry(QtCore.QRect(-220, -30, 1031, 600))
label3.setPixmap(QtGui.QPixmap("2.jpeg"))
label3.setObjectName("label")


label3 = QtWidgets.QLabel(win)
label3.setText("APRIL 2.0")
label3.resize(100,100)
label3.setGeometry(QtCore.QRect(20, 30,100,100))
label3.setObjectName("label")



myline=QtWidgets.QLineEdit(win)
myline.setPlaceholderText("google search")
myline.move(470,20) 
myline.resize(250,25)

myline2=QtWidgets.QLineEdit(win)
myline2.setPlaceholderText("wikipedia search")
myline2.move(470,45) 
myline2.resize(250,25)

l1=QtWidgets.QTextEdit(win)
l1.setPlaceholderText("this is the result bar")
l1.move(470,100)
l1.setFixedSize(300,500)

b1=QtWidgets.QPushButton(win)
b1.clicked.connect(action)
b1.setText("search")
b1.setFixedSize(60,25)
b1.move(725,20)



b2=QtWidgets.QPushButton(win)
b2.clicked.connect(action2)
b2.setText("search")
b2.setFixedSize(60,25)
b2.move(725,45)



win.show()
sys.exit(app.exec_())
