from __future__ import with_statement
import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import smtplib
import json
import pytz
import calendar
from email.message import EmailMessage

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


speak("What can I do for you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if 'stop everything' in query:
            speak("Stopping the program. Goodbye!")
            exit()
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def search_files(query):
    speak("Sure, please specify the name of the file.")
    file_name = query
    for root, dirs, files in os.walk("C:\\"):  # Change "C:\\" to the root directory you want to search
        for file in files:
            if file_name.lower() in file.lower():
                os.startfile(os.path.join(root, file))
                speak(f"Opening {file_name}")
                return
    speak(f"Sorry, I couldn't find a file named {file_name}.")


def send_email(receiver_email, subject, body):
    try:
        # Add your email credentials
        EMAIL_ADDRESS = "shreyasm101@gmail.com"
        EMAIL_PASSWORD = "Agent@sh101"

        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email sent successfully!")
            speak("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
        speak("Sorry, an error occurred while sending the email.")




def set_reminder():
    speak("Please provide the reminder details.")
    speak("What should I remind you about?")
    reminder_subject = takeCommand()
    speak("When should I remind you? Please specify the date and time.")
    reminder_date = takeCommand()
    # Add code to set the reminder using calendar or reminder services


def play_music():
    speak("Sure, please specify the name of the song.")
    song_name = takeCommand()
    speak(f"Playing {song_name} on YouTube.")
    kit.playonyt(song_name)


def get_news():
    try:
        # Add your News API key
        api_key = "e679e7c02f954ad98a6c8aab420d08f4"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles']
            speak("Here are the top headlines for today:")
            for article in articles:
                title = article['title']
                speak(title)
                print(title)
        else:
            speak("Sorry, I couldn't fetch the latest news.")
    except Exception as e:
        print("An error occurred while fetching news:", str(e))
        speak("Sorry, an error occurred while fetching news.")




if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            speak("yes sir")

        elif 'wikipedia' in query:
            speak('What would you like to search on Wikipedia?')
            search_query = takeCommand()
            speak('Searching Wikipedia...')
            try:
                results = wikipedia.summary(search_query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.WikipediaException as e:
                speak("Sorry, I encountered an error while searching on Wikipedia. Please try again later.")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'open youtube' in query:
            play_music()

        elif 'open file' in query:
            search_files(query)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Ready for calculation. Please speak the expression.")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                expression = r.recognize_google(audio)
                print("Expression:", expression)
                # Try to evaluate the expression
                try:
                    result = eval(expression)
                    speak(f"The result of {expression} is {result}")
                except Exception as e:
                    print("Error during evaluation:", str(e))
                    speak("Sorry, an error occurred during calculation.")

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the expression.")
                speak("Sorry, I couldn't understand the expression.")

            except Exception as e:
                print("An error occurred:", str(e))
                speak("Sorry, an error occurred during calculation.")

        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "refresh" in query:
            pyautogui.moveTo(1551, 551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620, 667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

        elif "who are you" in query:
            print('My Name Is Beta')
            speak('My Name Is Beta')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')

        elif "who created you" in query:
            print('I Do not Know His ')
            speak('I Do not Know His Name, I created with Python Language, inVisual Studio Code.')

        elif 'send email' in query:
            speak("To whom should I send the email?")
            receiver_email = takeCommand()
            speak("What should be the subject of the email?")
            subject = takeCommand()
            speak("What should be the content of the email?")
            body = takeCommand()
            send_email(receiver_email, subject, body)

        elif 'set reminder' in query:
            set_reminder()

        elif 'play music' in query:
            play_music()

        elif 'get news' in query:
            get_news()

