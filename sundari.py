import os
from urllib.parse import quote_from_bytes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")

    speak("I am sundari, your personal assistant.How may I help you!")

def takeCommand():
    '''
        It takes microphone input from the user and returns the string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        print(e)

        print("Say that again please!")
        return None

    return query

def sendEmail(to,content):
    # use of smtplib
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail(to,content)
    server.close()


if __name__=="__main__":
    # speak("Hello User")
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            # print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            webbrowser.open('spotify.com')

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'shubhamrthombare@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry I was unable to send the email.")