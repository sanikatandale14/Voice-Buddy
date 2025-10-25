# ==== Importing all the necessary libraries
import speech_recognition as sr

import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk


# ==== Class Assistant
class assistance_gui:
    def __init__(self,root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="images/background.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="images/frame_image.jpg")
        left = Label(self.root, image=self.centre).place(x=100, y=100, width=400, height=400)

        # ====start button
        start = Button(self.root, text='START', font = ("times new roman", 14), command=self.start_option).place(x=150, y=520)

        # ====close button
        close = Button(self.root, text='CLOSE', font = ("times new roman", 14), command=self.close_window).place(x=350, y=520)

    # ==== start assitant
    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        # ==== Voice Control
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        # ====Default Start
        def start():
            # ==== Wish Start
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak('Hello Sir,' + wish+' I am your voice assistant. Please tell me how may I help you')
            # ==== Wish End

        # ==== Take Command
        def take_command():
            try:
                print("Checking microphone...")
                with sr.Microphone() as data_taker:
                    print("Adjusting for ambient noise... Please wait...")
                    listener.adjust_for_ambient_noise(data_taker, duration=2)
                    print("Ready! Say Something...")
                    voice = listener.listen(data_taker, timeout=5, phrase_time_limit=5)
                    print("Processing your speech...")
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    print(f"I heard: {instruction}")
                    return instruction
            except sr.RequestError:
                print("Could not request results; check your internet connection")
                speak("Sorry, I'm having trouble connecting to the internet")
                return ""
            except sr.UnknownValueError:
                print("Could not understand the audio")
                return ""
            except Exception as e:
                print(f"Error: {str(e)}")
                return ""

        # ==== Run command
        def run_command():
            instruction = take_command()
            print(instruction)
            # if nothing recognized, ask user to speak again
            if not instruction:
                speak('I did not catch that, please say that again')
                return True
            try:
                if 'who are you' in instruction:
                    speak('I am your personal voice Assistant')

                elif 'what can you do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'current time' in instruction:
                    time = datetime.datetime.now().strftime('%I: %M')
                    speak('current time is' + time)

                # Broaden matching to accept variations like 'open google',
                # 'open google chrome', 'open chrome', or simply 'google'
                elif 'google' in instruction:
                    speak('Opening Google')
                    webbrowser.open('https://www.google.com')

                elif 'youtube' in instruction:
                    speak('Opening Youtube')
                    webbrowser.open('https://www.youtube.com')

                elif 'facebook' in instruction:
                    speak('Opening Facebook')
                    webbrowser.open('https://www.facebook.com')

                elif 'python geeks' in instruction or 'pythongeeks' in instruction:
                    speak('Opening PythonGeeks')
                    webbrowser.open('https://www.pythongeeks.org')

                elif 'linkedin' in instruction:
                    speak('Opening Linkedin')
                    webbrowser.open('https://www.linkedin.com')

                elif 'gmail' in instruction:
                    speak('Opening Gmail')
                    webbrowser.open('https://mail.google.com')

                elif 'stack overflow' in instruction or 'stackoverflow' in instruction:
                    speak('Opening Stack Overflow')
                    webbrowser.open('https://stackoverflow.com')

                elif 'shutdown' in instruction:
                    speak('I am shutting down')
                    self.close_window()
                    return False
                else:
                    speak('I did not understand, can you repeat again')
            except:
                speak('Waiting for your response')
            return True

        # ====Default Start calling
        start()

        # ====To run assistance continuously (call run_command once per loop)
        while True:
            if not run_command():
                break


    # ==== Close window
    def close_window(self):
        self.root.destroy()

# ==== create tkinter window
root = Tk()


# === creating object for class
obj=assistance_gui(root)

# ==== start the gui
root.mainloop()