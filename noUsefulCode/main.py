import os
from time import sleep
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="pl", slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

