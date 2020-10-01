import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir,Please tell me how may i help you")


def takeCommand():
    #It takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()

    #If True, ...(You can replace it with while loop if you want to keep repeating it)
    if 1:

        query=takeCommand().lower()

        #Logic fot executing based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
         
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
        
        elif 'open free code camp' in query:
            webbrowser.open("freecodecamp.org")
        
        elif 'open amazon.com' in query:
            webbrowser.open("amazon.com")
        
        elif 'open amazon prime' in query:
            webbrowser.open("primevideo.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        
        elif 'ud gaye' in query:
            webbrowser.open("https://www.youtube.com/watch?v=v2-9rIL_f4w")

            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is{strTime}")
        
        elif 'open code' in query:
            codePath="C:\\Users\\abhis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'shutdown' in query:
            speak("shutting down")
        
        


        
        
        







