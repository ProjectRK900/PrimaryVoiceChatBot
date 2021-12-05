# Part of the program to test mechanics of speech-to-text conversion
# Часть программы для проверки механики преобразования речи в текст

import speech_recognition as sr

voice_recognizer = sr.Recognizer()
with sr.Microphone() as source:
    # Микрофон используется программой
    voice_recognizer.adjust_for_ambient_noise(source) # - фикс шумов
    audio = voice_recognizer.listen(source)

# Микрофон снова доступен остальным программам
voice_text = voice_recognizer.recognize_google(audio, language="ru")
# print(voice_text) - проверка распознования