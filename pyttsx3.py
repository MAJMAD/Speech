#https://www.youtube.com/watch?v=buoSzgX9yM4&t=103s

import pyttsx3

text_speech = pyttsx3.init()

answer = input("what do you want to convert to speech :")
text_speech.say(answer)
text_speech.runAndWait()