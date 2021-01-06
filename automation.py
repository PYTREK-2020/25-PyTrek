import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os

engine = pyttsx3.init()


def speak(voice):
    engine.say(voice)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    mint = int(datetime.datetime.now().minute)
    sec = int(datetime.datetime.now().second)
    if (hour >= 0) and (hour <= 12):
        speak('good morning. Now the time' + str(hour) + 'hours' + str(mint) + 'minutes and ' + str(sec) + 'seconds')
    elif (hour > 12) and (hour <= 17):
        speak('good afternoon. Now the time' + str(hour) + 'hours' + str(mint) + 'minutes and ' + str(sec) + 'seconds')

    else:
        speak('good evening. Now the time' + str(hour) + 'hours' + str(mint) + 'minutes and ' + str(sec) + 'seconds')


def recogniser():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='en-in')
        print(data)

    except Exception as exp:
        print(exp)
        print('say again')
        return 0
    return data


if __name__ == '__main__':

    speak(' how are you ')
    while True:
        query = recogniser().lower()
        # print(query)
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open code' in query:
            os.startfile('C:\\Users\\SAMSUNG\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
        elif 'close' or 'exit' in query:
            break














