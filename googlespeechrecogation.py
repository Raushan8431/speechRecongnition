import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
import webbrowser

listening = sr.Recognizer()
engine = pt.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd = ""  # Initialize cmd with an empty string
    try:
        with sr.Microphone() as mic:
            print('listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'raushan' in cmd:
                cmd = cmd.replace('raushan','')
                print(cmd)
    except Exception as e:
        print("Error:", e)
        pass
    return cmd

def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('playing ' + song)
        pk.playonyt(song)
    elif 'search' in cmd:
        query = cmd.replace('search', '')
        speak('Searching for ' + query)
        pk.search(query)
    else:
        # Perform a Google search with the whole command if neither 'play' nor 'search' is detected
        speak('Searching for ' + cmd)
        pk.search(cmd)

run()


