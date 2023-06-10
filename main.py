import speech_recognition as sr
import pyttsx3
import webbrowser


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. Give a command...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Recognized command: " + text)
        return text
    except sr.UnknownValueError:
        print("Command not understood.")
        return ""


def speak(text, voice_id):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
        engine.say(text)
        engine.runAndWait()
    else:
        print("Invalid voice_id: " + str(voice_id))


def open_website(url, voice_id):
    speak("Opening website...", voice_id)
    webbrowser.open(url)


def close_website(voice_id):
    speak("Closing website...", voice_id)
    webbrowser.close()


while True:
    command = listen()

    if "hello" in command:
        speak("Hello, how can I assist you?", 0)  # Use the first voice
    elif "how are you" in command:
        speak("I'm an artificial intelligence, so I don't have feelings, but thank you. How can I assist you?",
              1)  # Use the second voice
    elif "Google" in command:
        open_website("https://www.google.com", 0)  # Use the first voice
    elif "1" in command:
        close_website(0)
    elif "YouTube" in command:
        open_website("https://www.youtube.com", 0)  # Use the first voice
    elif "Close Youtube" in command:
        close_website(0)  # Use the first voice
    elif "Kafkas" in command:
        open_website("https://obsyeni.kafkas.edu.tr/", 0)
    elif "Close kafkas" in command:
        close_website(0)
    elif "Discord" in command:
        open_website("https://discord.com/channels/@me", 0)
    elif "Close discord"in command:
        close_website(0)
    elif "Ziraat" in command:
        open_website("https://bireysel.ziraatbank.com.tr/Transactions/Login/FirstLogin.aspx?ReturnUrl=%2fDefault.aspx", 0)
    elif "Close Ziraat" in command:
        close_website(0)
    elif "Spotify" in command:
        open_website("https://open.spotify.com", 0)
    elif "Close Spotify" in command:
        close_website(0)
    elif "stop" in command.lower():
        break
    else:
        speak("Sorry, I didn't understand. Please repeat.", 0)  # Use the first voice
