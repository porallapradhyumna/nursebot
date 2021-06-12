# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:42:13 2021

@author: PRADHYUMNA
"""

import cv2
import speech_recognition as sr
from Recive_Response import SpeechAndReply as s
from object_detection import Object_Detection as od
from FaceRecognition1 import FaceRecognition as fr
from Face_Detection import Face_Detection as fd
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
from datetime import datetime
import weather
from playsound import playsound

cap = cv2.VideoCapture(0)
bot = ChatBot(
        'Medizoid',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        
    )
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
names=[]
times=[]
while True:
       
    instance,name=fr.Recognizer(cap)
    r = sr.Recognizer()
    text = s.Recogniser(r)
    print(text)
    
    if name not in names:
        names.append(name)
        times.append(time.time())
        s.Reply("Hello "+ name.lower())
    elif name in names:
        idx=names.index(name)
        timex=times[idx]
        diff = time.time()-timex
        if int(diff)>600:
            names.pop(idx)
            times.pop(idx)
    else:
        continue
    
        
    if text == "what can you see":
        objects=od.Object_Detection(cap)
        obj_list=", ".join(objects)
        content = "I can see "+str(obj_list)
        s.Reply(content)
    elif "time" in text or "date" in text:
        time=datetime.now()
        tim = "Today date is"+str(time.dy)+","+str(time.month)+","+str(time.year)+"and time now is"+str(time.hour)+"hours"+str(time.minute)+"minutes"
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
        s.Reply(weather)
    elif "weather" in text:
        s.Reply(weather)
    else:
        bot_input = bot.get_response(text)
        print(str(bot_input))
        s.Reply(str(bot_input))                            
    #return names,times