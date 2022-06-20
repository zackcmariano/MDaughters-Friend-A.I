import pyttsx3


engine = pyttsx3.init()

#rate = engine.getProperty("rate")
#engine.setProperty("rate", 60)

voices = engine.getProperty("voices")


#engine.setProperty("voice", voices[0].id)

for voice in voices:
    print(voice.id, voice.name, voice.languages)

engine.setProperty("voice", "brazil")
engine.setProperty("rate", 20)
engine.setProperty("volume", 1.)



engine.say("")
engine.runAndWait()