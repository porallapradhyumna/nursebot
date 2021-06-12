# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:22:24 2020

@author: PRADHYUMNA
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
        'Medizoid',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'],
        database_uri='sqlite:///database.sqlite3'
        
    )
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
def chatty(text):
    lis = text.split(" ")
    for i in range(len(lis)-1):
        #print(lis[i-1],lis[i+1])
        if lis[i-1].isnumeric() and lis[i+1].isnumeric():
            if lis[i] == "into":
                lis[i] = "*"
            elif lis[i] == "by":
                lis[i] = "/"
    text = " ".join(lis)
    bot_input = bot.get_response(text)
    return str(bot_input)