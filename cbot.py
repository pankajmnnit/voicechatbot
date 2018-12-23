from chatterbot import ChatBot
import win32com.client as wincl
import speech_recognition as sr

from gtts import gTTS 
from chatterbot.trainers import ListTrainer
import os
r = sr.Recognizer()
bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)


speak = wincl.Dispatch("SAPI.SpVoice")
with sr.Microphone() as source:
 while True:
     
       print("Speak Anything :")
       audio=r.listen(source)  
       try:
         text=r.recognize_google(audio)
         print("You said : {}".format(text))
         reply=bot.get_response(""+text)
         speak.Speak(reply)
       except:
         print("Sorry could not recognize what you said")
         speak.Speak("can you repeat please")

     #if text.strip()=='Bye':
     #   printf('ChatBot:Bye')
      #  break
