import pyttsx3
import datetime
import speech_recognition as sr
#import pyaudio
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon....")
    else:
        speak("Good evening..")
    speak("Hii , I am javris how can i help you ")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said : {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please.....")
        return "None"
    return query
if __name__ == "__main__":

    wishMe()
    if 1:
            query=takeCommand().lower()

            if 'wikipedia' in query:
                speak('searching wikipedia...')
                query=query.replace("Wikipedia","")
                results=wikipedia.summary(query,sentences=5)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube'in query:
                webbrowser.open("youtube.com")
            elif 'open google'in query:
                webbrowser.open("google.com")
            elif 'open stackoverflow'in query:
                webbrowser.open("stackoverflow.com")
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is:{strTime}")
            elif 'open code' in query:
                code_path="C:\\Users\\91700\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
            

            
            
            





