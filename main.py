import speech_recognition as sr
import playsound as ps
import gtts
import os

# all Functions:
# voice input from user and convert it to text
def user_input(whichLang):
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        print('Слушаю...')
        audio = voice_recognizer.listen(source)
        voice_text = voice_recognizer.recognize_google(audio, language=whichLang)

    voice_text = voice_text.lower()
    return voice_text

# program sound something (available diff languages)
def soundOn(someText, whichLang):
    voice = gtts.gTTS(someText, lang=whichLang)
    audio_file = 'TempAudio.mp3'
    voice.save(audio_file)
    print('Ответ...')
    ps.playsound(audio_file)
    os.remove(audio_file)

# answer choice (answers can be added endlessly)
def switch(text):
    if text == "привет" or text == "hi" or text == "hello":
        soundOn('Hi', 'en-GB')
    elif text == "пока" or text == "goodbye" or text == "bye":
        soundOn('See you soon', 'en-GB')
        exit()
    elif text == "имя" or text == "name":
        soundOn('Primary Jarvis, Version: 0.0.0.0.1', 'en-GB') # version is joke ;D
    elif text == "повтори":
        print('    Ваша фраза:')
        usersText = user_input('ru')
        print(usersText)
        soundOn(usersText, 'ru')
    elif text == "repeat":
        print('Your quote:')
        usersText = user_input('en-GB')
        print(usersText)
        soundOn(usersText, 'en-GB')
    elif text == "помощь" or text == "help":
        print("""Привет/Hi/Hello - приветствие
Пока/GoodBye/Bye - прощание (конец программы)
Имя/Name - представиться
Повтори/Repeat - повторить фразу после команды""")
    else:
        soundOn('Неизвестная команда', 'ru')
        print('Используйте команды "Help" или "Помощь" для получения списка доступных команд')

# repeat program
def start(lang):
    while True:
        usersText = user_input(lang)
        print(usersText)
        switch(usersText)

# finally the program
lang = input('\nВыберите язык: ')
start(lang)
