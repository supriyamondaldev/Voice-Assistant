import os
import pyttsx3
import speech_recognition as sr
import subprocess
import webbrowser
import threading
import time
import datetime
import wikipedia
import pyaudio

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Global flags
is_active = False
stop_listening = False


def speak(text):
    """Speak the given text"""
    engine.say(text)
    engine.runAndWait()


def check_for_enter():
    """Check for Enter key press to stop listening"""
    global stop_listening
    input("\n[⏹ Press Enter to stop listening...]")  # Wait for Enter key press
    stop_listening = True


def recognize_speech():
    """Recognize speech using Google Recognizer"""
    global stop_listening
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n[ Listening...] (Press Enter to stop)")
        if not is_active:
            print("[Waiting for 'Jarvis']")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        stop_listening = False
        key_thread = threading.Thread(target=check_for_enter)
        key_thread.daemon = True
        key_thread.start()

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("[🟢 Timeout: 5 seconds of silence]")
            return ""
        except Exception as e:
            print(f"Error: {str(e)}")
            return ""

        stop_listening = False

        try:
            return recognizer.recognize_google(audio, language="en-in").lower()
        except sr.UnknownValueError:
            print("[🟡 Couldn't understand audio]")
            return ""
        except sr.RequestError:
            speak("[Google API request failed. Check your internet connection]")
            return ""
        return ""

def greet_user():
    """Greet the user based on the time of day"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")

    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")



def get_time():
    """Tell the current time"""
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")


def get_date():
    """Tell the current date"""
    now = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {now}")


def search_wikipedia(query):
    """Search Wikipedia and return a summary"""
    speak("Searching Wikipedia...")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia: ")
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results, please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find anything on Wikipedia about that.")


def open_website(website_name):
    """Open a website in the default browser"""
    url = f"https://www.{website_name}.com"
    webbrowser.open(url)
    speak(f"Opening {website_name}")

def open_websites(website_names):
    """Open a website in the default browser"""
    url = f"https://www.{website_names}.in"
    webbrowser.open(url)
    speak(f"Opening {website_names}")

def open_websitess(website_namess):
    """Open a website in the default browser"""
    url = f"https://www.{website_namess}.net"
    webbrowser.open(url)
    speak(f"Opening {website_namess}")


def open_url(url_id):
    """Open a website in the default browser"""
    url = f"{url_id}"
    webbrowser.open(url)
    speak("Opening")


def jarvis():
    print("Hello! I am Jarvis, your smart assistant. Say 'Jarvis' to activate me")
    global is_active
    speak("Hello! I am Jarvis, your smart assistant. Say 'Jarvis' to activate me.")

    while True:
        command = recognize_speech().strip()
        if not command:
            continue

        print(f"[🟢 Heard: {command}]")

        # Check for wake word
        if "jarvis" in command and not is_active:
            is_active = True
            speak("Yes, sir? How can I assist you?")
            greet_user()
            continue

        # Check for stop command
        if "stop" in command and is_active:
            is_active = False
            speak("Going silent. Say 'Jarvis' to wake me up again.")
            continue

        # Process commands only when active
        if is_active:
            if command in ["exit", "quit"]:
                speak("Goodbye! Have a nice day.")
                break
            elif "time" in command:
                get_time()
            elif "date" in command:
                get_date()
            elif "wikipedia" in command:
                search_wikipedia(command.replace("wikipedia", "").strip())
            elif "open youtube" in command:
                open_website("youtube")
            elif "open facebook" in command:
                open_website("facebook")
            elif "open google" in command:
                open_website("google")
            elif "open insta" in command:
                open_website("instagram")
            elif "open wikipedia" in command:
                open_website("wikipedia")
            elif "open iemcrp" in command:
                open_website("iemcrp")
            elif "open linkedin" in command:
                open_website("linkedin")
            elif "open amazon" in command:
                open_websites("amazon")
            elif "open slideshare" in command:
                open_websitess("slideshare")
            elif "open whatsapp" in command:
                open_website("whatsapp")
            elif "open chat gpt" in command:
                open_website("chatgpt")
            elif "open github" in command:
                open_website("github")
            elif "open gmail" in command:
                open_website("gmail")
            elif "play achcha chalta hun on youtube" in command:
                open_url("https://youtu.be/bzSTpdcs-EI?si=x-h5vgO5dBzuO_FN")
            elif "play national anthem" in command:
                open_url("https://youtu.be/HtMF973tXIY?si=YsvGyzKAegkb5kTC")
            elif "play its you" in command:
                open_url("https://www.youtube.com/watch?v=PXGycbkbtW0")
            elif "play we don't talk anymore" in command:
                open_url("https://www.youtube.com/watch?v=3AtDnEC4zak")
            elif "play yeh tara woh tara" in command:
                open_url("https://www.youtube.com/watch?v=9UzvpM3IwwY")
            elif "play tere naina" in command:
                open_url("https://www.youtube.com/watch?v=uc43tD6-E4U")
            elif "play sajda" in command:
                open_url("https://www.youtube.com/watch?v=3rPEWcY6Oww")
            elif "play jiya re" in command:
                open_url("https://www.youtube.com/watch?v=smn3mDBOUy4")
            elif "play noor e khuda" in command:
                open_url("https://www.youtube.com/watch?v=JJ5r5Z6G2Zo")
            elif "play saas" in command:
                open_url("https://www.youtube.com/watch?v=VAt6TO2gdko&list=RDGMEM2j3yRsqu_nuzRLnHd2bMVA&start_radio=1&rv=JJ5r5Z6G2Zo")

            else:
                speak("I'm sorry, I don't understand that command.")
        else:
            print("[Waiting for activation...]")


if __name__ == "_main_":
    jarvis()