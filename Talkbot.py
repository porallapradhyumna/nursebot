
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:00:11 2020

@author: PRADHYUMNA
"""

import numpy as np
import pandas as pd
import platform,os
from datetime import datetime
import speech_recognition as sr
from playsound import playsound
from Recive_Response import SpeechAndReply as s
import time
import Chat as ch
import wikipedia 
import pywhatkit


dataset = pd.read_csv('Talkbot.csv')
x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 3].values
x = x.tolist()
y = y.tolist()

for n,i in enumerate(x):
    x[n]=i.lower()
for n,i in enumerate(y):
    y[n]=i.lower()
    
    
def Talkbot(text):    
    if "update" in text :
        text = text.replace("update","")
    print(text)
    if text != "":
        if text in x:
            idx = x.index(text.lower())
            s.Reply(y[idx])
        elif "can you hear" in text:
            s.Reply("yes I can hear you")
        elif "time" in text or "date" in text:
            time=datetime.now()
            tim = "Today date is"+str(time.day)+","+str(time.month)+","+str(time.year)+"and time now is"+str(time.hour)+"hours"+str(time.minute)+"minutes"
            s.Reply(tim)
        elif "end" in text or "exit" in text:
            playsound("havegreatday.mp3")
            
        elif "system" in text:
            uname=platform.uname()
            syst = " system "+uname.system+" node "+uname.node+" release "+uname.release+" version "+str(uname.version)+" machine "+str(uname.machine)+" processor "+str(uname.processor)
            s.Reply(syst)
        elif "temperature" in text:
            import weather 
            temp,weather = weather.Temp_Response()
            print(temp)
            s.Reply(temp)
        elif "weather" in text:
            import weather 
            temp,weather = weather.Temp_Response()
            print(weather)
            s.Reply(weather)
        elif "search for" in text or "search" in text:
            txt = text.split()
            txt.remove("search")
            txt.remove("for")
            text = " ".join(txt)
            result = wikipedia.summary(text, sentences = 2)
            s.Reply(result)
                    
        elif "play" in text or "song" in text:
            txt = text.split()
            if "play" in txt:
                txt.remove("play")
            elif "song" in txt : 
                txt.remove("song")
            elif "of" in txt:
                txt.remove("of")
            text = " ".join(txt)
            pywhatkit.playonyt(text)
                
        else:
            reply  = ch.chatty(text)
            s.Reply(reply)
                    #s.Reply("Sorry ! I am still learning or Please say it again")
                    #break
    else:
        s.Reply("Something went wrong")
    
def Master_adaptive():    
    while True:
        playsound("continue.mp3")
        r = sr.Recognizer()
        text = s.Recogniser(r)
        print(text)
        try:
            if text in x:
                idx = x.index(text.lower())
                s.Reply(y[idx])
            elif "time" in text or "date" in text:
                time=datetime.now()
                tim = "Today date is"+str(time.day)+","+str(time.month)+","+str(time.year)+"and time now is"+str(time.hour)+"hours"+str(time.minute)+"minutes"
                s.Reply(tim)
            elif "end" in text or "exit" in text:
                playsound("havegreatday.mp3")
                break
            elif "system" in text:
                uname=platform.uname()
                syst = " system "+uname.system+" node "+uname.node+" release "+uname.release+" version "+str(uname.version)+" machine "+str(uname.machine)+" processor "+str(uname.processor)
                s.Reply(syst)
            elif "temperature" in text:
                temp,weather = weather.Temp_Response()
                s.Reply(temp)
            elif "weather" in text:
                temp,weather = weather.Temp_Response()
                s.Reply(weather)
            elif "search for" in text or "search" in text:
                txt = text.split()
                txt.remove("search")
                txt.remove("for")
                text = " ".join(txt)
                result = wikipedia.summary(text, sentences = 2)
                s.Reply(result)
            else:
                s.Reply("Sorry ! I am still learning or Please say it again")
                    #break
        except:
            s.Reply("Something went wrong")
            
if __name__ == "__main__":
    while True:
        
        r = sr.Recognizer()
        text = s.Recogniser(r)
        
        if "impulse" in text:
            lis=text.split()
            lis.remove("impulse")
            text=" ".join(lis)
            try:
                Talkbot(text)
            except :
                pass
        elif "google" in text or "alexa" in text or "Alexa" in text or "Google" in text:
            playsound("sorry_Im_missPulse.mp3")
        