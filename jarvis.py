import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import pyaudio

chrome_path = "C:/Users/USER/AppData/Local/Google/Chrome/Application/chrome.exe %s"



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("todays date is")
    speak(day)
    speak(month)
    speak(year)
    print("todays date is : ", day , month , year)



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir !")
        
    else:
        speak("Good Evening Sir !")
    speak("I am Emily. How may I help you !")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 300
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("User said: " , query)
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    # takeCommand()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        if 'tell me something about you' in query:
            speak("I am Emily , a personalised AI model, created by Siddharth Tripathi. I can help you in doing your usual task like opening or closing some website, opening apps et cetera.")
            
        elif 'I love you' in query:
            speak("I love you too, Siddharth.")
            
        elif 'do you love' in query:
            speak("i only love my master, Siddharth.") 
            
        elif 'do you like' in query:
            speak("i only like my master, Siddharth.")
            
        elif 'fall in love' in query:
            speak("yes , my master Siddharth.")
        
        elif 'who are you' in query:
            speak("I am Emily , a personalised AI model, created by Siddharth Tripathi")
            
        elif 'what are you' in query:
            speak("I am Emily , a personalised AI model, created by Siddharth Tripathi")
            
        elif 'who is your developer' in query:
            speak("my developer is Siddharth Tripathi")
            
        elif 'who is your creater' in query:
            speak("I am created by Siddharth Tripathi")    
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            speak("opening google home page")
            webbrowser.open("goolge.com")
            
        elif 'open bootstrap' in query:
            speak("opening bootstrap home page")
            webbrowser.open("getbootstrap.com")
            
        elif 'open email' in query:
            speak("opening email")
            webbrowser.open("gmail.com")
            
        elif 'music in browser' in query:
            speak("opening youtube and showing trending songs list. please select suitable music according to you.")
            webbrowser.open("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D") 
            
        elif 'song in browser' in query:
            speak("opening youtube in browser and showing trending songs list. please select suitable music according to you.")
            webbrowser.open("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D")
            
        elif 'song in youtube' in query:
            speak("opening youtube and showing trending songs list. please select suitable music according to you.")
            webbrowser.open("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D")
            
        elif 'music in youtube' in query:
            speak("opening youtube and showing trending songs list. please select suitable music according to you.")
            webbrowser.open("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D")
            
        elif 'open chat gpt' in query:
            speak("opening chat gpt in browser")
            webbrowser.open('https://chatgpt.com/')
            
        elif 'play music' in query:
            speak("opening music directary")
            music_dir = 'C:\\Users\\USER\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is : {strTime} ")
            
        elif 'date' in query:
            date()
            
        elif 'open code' in query:
            speak("opening visual studio code")
            codePath = 'C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        
        
        elif 'open visual studio code' in query:
            speak("opening visual studio code")
            codePath = 'C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
            
        elif 'open vs code' in query:
            speak("opening visual studio code")
            codePath = 'C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
            
        elif 'open word' in query:
            speak("opening word")
            codePath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(codePath)
            
        elif 'open powerpoint' in query:
            speak("opening powerpoint")
            codePath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(codePath)
            
        elif 'exit' in query:
            speak("shutting down")
            exit()
            
        elif 'you can stop' in query:
            speak("Ok , shutting down , goodbye master")
            exit()
            
        elif 'you may leave' in query:
            speak("Ok , shutting down , goodbye master")
            exit()
            
        elif 'shut up' in query:
            speak("Sorry Master , shutting down")
            exit()
            
        elif 'search' in query:
            speak("what should I search?")
            search = takeCommand().lower()
            webbrowser.get(chrome_path).open_new_tab(search + ".com")
        
        
    # ----------------------PYAUTOGUI features----------------------
    
        elif 'hidden menu' in query:
            speak("opening hidden menu")
            pyautogui.hotkey('winleft' , 'x')
            
        elif 'task manager' in query:
            speak("opening task manager")
            pyautogui.hotkey('ctrl' , 'shift' , 'esc')
            
        elif 'task view' in query:
            speak("opening task view")
            pyautogui.hotkey('winleft' , 'tab')
            
        elif 'screenshot' in query:
            speak("taking screenshot")
            img = pyautogui.screenshot()
            img.save("C:/Users/USER/Pictures/Screenshot by AI/AIscreenshot.png")
            speak("done")
            
        elif 'snip' in query:
            speak("opening snip interface")
            pyautogui.hotkey('winleft' , 'shift' , 's')
            
        elif 'close the app' in query:
            speak("closing the current application")
            pyautogui.hotkey('alt' , 'f4')
        
        