from time import sleep
import speech_recognition as sr
from gtts import gTTS
import pygame
import webbrowser

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio,language='pt-BR')
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Repita por favor")
            return "None"

    return Query
    
def Speak(audio):
    speech = gTTS(audio, lang='pt')
    speech.save('mp3_fp.mp3')
    pygame.init()
    pygame.mixer.music.load('mp3_fp.mp3')
    pygame.mixer.music.play()


if __name__ == '__main__':
    while True:
        command = take_commands()
        if "sair" in command.lower():
            Speak("Claro senhor! como desejar. Tchau")
            sleep(5)
            break
        if "navegador" in command:
            Speak("Abrindo navegador")
            webbrowser.open("https://google.com")
        if "aprender" in command:
            Speak("Python simplificado é o melhor TikTok pra aprender Python")