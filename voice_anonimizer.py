# Anonimizer is independently part of the program which
#   identify voice message and repeat it in console
#   and sound output

# Anonimizer - самостоятельная часть программы, которая
#   распознаёт голосовое сообщение и повторяет его в
#   кносоль и вывод звуков

import speech_recognition as sr
import playsound as ps
import gtts
import os

def user_input():
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # voice_recognizer.adjust_for_ambient_noise(source)
        audio = voice_recognizer.listen(source)
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
    return voice_text

def reply(text):
    voice = gtts.gTTS(text, lang="ru")
    audio_file = 'audio.mp3'
    voice.save(audio_file)

    ps.playsound(audio_file)
    os.remove(audio_file)

newInputText = user_input()
print(newInputText)
reply(newInputText)