# https://github.com/ProgrammingHero1/audiobook

import pyttsx3 # pip install pyttsx3
import PyPDF2  # pip install PyPDF2
book = open('pdf-sample.pdf', 'rb')  # open read+binary
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    print("----")    
    speaker.say(text)
    speaker.runAndWait()
    