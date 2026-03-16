import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from dotenv import load_dotenv 
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import time


load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

#pip install pocketsphinx
#pip install python-dotenv

recognizer = sr.Recognizer()


def speak_old(text):
    engine.say(text)
    engine = pyttsx3.init()
    engine.runAndWait()
    
    
def speak(text):
    try:
        tts = gTTS(text=text, lang="en")
        tts.save("temp.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove("temp.mp3")

    except Exception as e:
        print("Speech Error:", e)


def aiProcess(command):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:0.5b",
            "prompt": command,
            "stream": False
        }
    )

    data = response.json()
    return data["response"]


print(aiProcess("Explain coding in simple words"))



# responses through paid version of API Key   
''' 
def aiProcess(command):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. Give short responses"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content
'''



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play ", "")

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Song not found")
    elif "news" in c.lower():
       url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_API_KEY}"
       r = requests.get(url)
       if(r.status_code== 200):
           # parse the jason response
           data = r.json()
           # Extract the articles
           articles = data.get('articles', [])
           # print the headlines
           for article in articles:
               speak(article['title'])
               
    else:
        # Let openAI handle the request
        output = aiProcess(c)
        speak(output)
     
    
if __name__ == "__main__":
    speak("Initializing zoro....")
    while True:
        # Listen for the wake word zoro
        # obtain audio from the microphone
        r = sr.Recognizer()
        
            
            
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)

  
            if(word.lower() == "zoro"):
                speak("Yes")
                # listen for command
                with sr.Microphone() as source:
                    print("zoro is Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
        except sr.WaitTimeoutError:
            continue

        except sr.UnknownValueError:
            print("Could not understand audio")

        except Exception as e:
            print("Error:", e)
 