# Part of the program to test mechanics of text-to-speech conversion
# Часть программы для проверки механики преобразования текста в речь

import playsound
import gtts
import os

text = 'Привет'

voice = gtts.gTTS(text, lang="ru")
audio_file = 'audio.mp3'
voice.save(audio_file)

playsound.playsound(audio_file)
os.remove(audio_file)
