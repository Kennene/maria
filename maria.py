# -*- coding: utf-8 -*-
from dotenv import load_dotenv                  # Ładowanie zmiennych środowiskowych z pliku .env
import os                                       # Biblioteka suplementująca load_dotenv
import pygame                                   # Odtwarzanie plików dźwiękowych .wav
import threading                                # Wątkowanie odgłosów dźwiękowych
import speech_recognition                       # Przekształcanie mowy na tekst
from openai import OpenAI                       # ChatGPT API
from TTS.utils.manage import ModelManager       # Modele językowe
from TTS.utils.synthesizer import Synthesizer   # Odtwarzacz modeli
# Written in Python 3.11.2


def dev(message):
    print("...>"+message)


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)                         # Dostosowanie środowiska użytkownika do realnego
        dev("Listening for user's input")
        audio = recognizer.listen(source)                                   # Gromadzenie dźwięku użytkownika

    try:
        dev("Recognizing user's input")
        user_input = recognizer.recognize_google(audio, language="en-US")   # Przekształcanie zgromadzonej mowy na tekst
        dev("User said: " + user_input)

    except speech_recognition.UnknownValueError:
        dev("Program couldn't resolve user's speech to text")
        user_input = "-1"

    except speech_recognition.RequestError as e:
        dev("Google is unavailable at the moment: ".format(e))
        user_input = "-2"

    return user_input.lower();


def play_wav_async(path):
    pygame.mixer.init()                     # Załadowanie mixera pygame

    try:
        sound = pygame.mixer.Sound(path)    # Wczytanie pliku do pamieci
        sound.play()                        # Uruchomienie odtwarzania
        while pygame.mixer.get_busy():      # Podczas gdy odtwarzacz jest zajęty...
            continue                        # nie przestawaj przetwarzać programu
        pygame.quit()

    except pygame.error:
        dev("Error playing given sound at: " + path)


def chatGPT(prompt):
    context = os.getenv("CONTEXT")
    response = OpenAI().chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
             "role": "system",
             "content": context
            },

            {
             "role": "user",
             "content": prompt
            }
        ],
        temperature=0,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


def speak(text):
    path = "response.wav"       # Ścieżka do zapisania wygenerowanego pliku dźwiękowego
    outputs = syn.tts(text)    # Przekształcenie tekstu na dźwięk
    syn.save_wav(outputs, path) # Zapisanie dźwięku do pliku
    play_wav_async(path)        # Odtworzenie zapisanego pliku


def graphical(message):
    avatar = """
     \_\\
    (_**)
   __) #_
  ( )...()
  || | |I|
  || | |()__/
  /\(___)
_-\"\"\"\"\"\"\"-_\"\"-_
-,,,,,,,,- ,,,-
"""
    print(message)
    print(avatar)



if __name__ == "__main__":
    load_dotenv()                                   # Inicjacja zmiennych środowiskowych z .env
    recognizer = speech_recognition.Recognizer()    # Inicjacja rozpoznawacza mowy
    pygame.init()                                   # Załadowanie podstawowego silnika pygame

    # Aby zobaczyć dostępne opcje należy wpisać tts --list_models
    model_manager = ModelManager("venv/lib/python3.11/site-packages/TTS/.models.json")                    # Miejsce do zapisywania modeli
    model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")  # Zapisz model głosowy
    voc_path, voc_config_path, _ = model_manager.download_model('vocoder_models/en/ljspeech/hifigan_v2')        # Zapisz model vocoder

    syn = Synthesizer( #Opcje syntezatora mowy
        tts_checkpoint=model_path,
        tts_config_path=config_path,
        vocoder_checkpoint=voc_path,
        vocoder_config=voc_config_path
    )

    while True:

        if 'maria' in listen():

            threading.Thread(target=play_wav_async, args=("activate.wav",)).start() # Asynchronicznie uruchom dźwięk
            command = listen()                                                      # Odczytaj prompt wysyłany do ChatGPT

            if command != "nieważne":                                               # Wyjdź z poziomu zapytywania
                if command == '-1' or command == '-2':                              # Jeżeli otrzymano niezrozumiałe dane z funkcji słuchającej
                    dev("Skipping querying prompt to ChatGPT")
                else:                                                               # Jeżeli poprawnie odsłuchano zapytanie
                    dev("User said:\n" + command)
                    response = chatGPT(command);                                    # Wysyłanie polecenie do ChatGPT i zczytywanie odpowiedzi
                    dev("ChatGPT responded:\n" + response)
                    graphical(response)                                             # Wyświetl graficznie odpowiedź
                    speak(response)                                                 # Powiedz na głos co zwrócił ChatGPT

                threading.Thread(target=play_wav_async, args=("exit.wav",)).start()     # Zakończ poziom zapytywania