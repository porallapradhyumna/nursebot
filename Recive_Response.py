 # -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:39:12 2020

@author: PRADHYUMNA
"""

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os 
import time
#import winsound
import concurrent.futures


class SpeechAndReply():
    @staticmethod
    def Reply(mytext):
        
        language="en"
        r = random.randint(1,1000000)
        audio_file = "audio-"+str(r)+".mp3"
        output=gTTS(text=mytext,lang=language,slow=False)
        output.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file)
       
    @staticmethod  
    def Recogniser(recognizer,phrase_time_limit=5):
        playsound('beep-07.mp3')
        r = recognizer
        try:
            with sr.Microphone(device_index =1) as source:
                audio = r.listen(source,phrase_time_limit=5)
                text = r.recognize_google(audio,language="en-IN")
                playsound('beep-07.mp3')
                return text
        except sr.UnknownValueError:
            return "Something went wrong , I cant hear"
        except sr.RequestError:
            return "Sorry I cant hear you"
        
#mytext = "Hello Master! How may I help you"
"""s = SpeechAndReply()
r = sr.Recognizer()
text = s.Recogniser(r,phrase_time_limit=2)

#playsound('beep-07.mp3')
try:
    s.Reply(text)
except:
    s.Reply("Something went wrong")"""
"""if __name__ == "__main__":    
    s = SpeechAndReply()
    r = sr.Recognizer()
    executor = concurrent.futures.ThreadPoolExecutor()
    future = executor.submit(s.Recogniser, r)
    text = future.result()
    print(text)
    
    future = executor.submit(s.Reply, text)
    text = future.result()
    """
    
    
