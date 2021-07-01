import pyttsx3   # pip install pyttsx3   
text = 'Hello nicolas'
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
