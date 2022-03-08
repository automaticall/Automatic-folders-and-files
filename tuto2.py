'''import packages'''
from multiprocessing.connection import Listener
from time import time
import databases
from matplotlib.pyplot import text
from setuptools import Command
import speech_recognition as sr 
import pyttsx3 as ttx
import sys
from datetime import datetime

'''My own packages '''
from foldersBuilder import *

'''Main moduls of speech recognition'''
# print(dir(sr))

'''init'''
Listener=sr.Recognizer()
engine=ttx.init()
engine.setProperty('voice',"french")
engine.setProperty('rate',170)
voice=engine.getProperty('voices')

'''talk'''
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
'''great me '''
def greatMe():
    Hour=int(datetime.now().hour)
    time=datetime.now().strftime("%H:%M")
    if 0<=Hour <12:
        text=f"Bonjour Laris!,il est {time}"
        talk(text)
    elif 12<=Hour<18:
        text=f"Bon après midi laris !, il est {time}"
        talk(text)
    else:
        text=f"Bonsoir laris!, il est {time}"
 
greatMe()
engine.say("comment tu vas ")
engine.runAndWait()

def lisener_():
    """_summary_
    this function return command as text
    """
    try:
        with sr.Microphone()as source:
            Listener.adjust_for_ambient_noise(source)
            voix=Listener.record(source,duration=5)
            command=Listener.recognize_google(voix,language="fr-FR")
            command.lower()
            if "larissa" in command:
                command=command.replace("larissa","")
    except sr.UnknownValueError:
        ttx.speak("Aurevoir!")
    return command

    """_summary_
    Assisstant vocal
    """
    
def AssisstantVocal():
    command=lisener_()
    if "et toi" in command:
        text="je vais bien aussi! merci"
        talk(text)
        
    elif "fais-moi" in command:
        text='vous vouliez créer quoi?'
        talk(text)
    elif "le fichier" in command:
        namenewFile_withoutExtention=command.replace("le fichier","")
        namenewFile=namenewFile_withoutExtention+".py"
        workdirectorie=os.getcwd()
        source=workdirectorie.replace("\\","/")
        main_file=file__(source,namenewFile)
        main_file.newFile_()
        text=namenewFile+"créer avec succès, Merci pour votre patience"
        talk(text)
    elif "désactive toi" in command:
        text="Aurevoir laris!"
        talk(text)
        sys.exit()
    else :
        talk('je ne comprends pas ce que vous dites, vueillez réessayer')
        
while True:
    AssisstantVocal()
        
        
        

