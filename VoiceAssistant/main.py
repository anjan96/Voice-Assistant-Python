import pyttsx3                               #pip install pyttsx3
import datetime
import speech_recognition as sr              #pip install speechRecognition
import wikipedia                             #pip install wikipedia
import webbrowser
import os
import smtplib                               #pip install secure-smtplib
from requests import get                       #pip install requests
import pywhatkit


from tkinter import *
from PIL import ImageTk

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def start():

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning sir!")
        elif hour>=12 and hour < 18:
            speak("Good Afternoon sir!")
        else :
            speak("Good Evening sir!")

    def introduce():
        speak("Hello sir. i am your voice assistant david")



    def TakeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source :
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language= 'en-US')
            print(f"user : {query}\n")

        except Exception as e :

            return "None"
        return query



    def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('anjandebnath96@gmail.com', 'sumitanjan')
        server.sendmail('anjandebnath96@gmail.com', to, content)
        server.close()


    def emailToAnjan():
        try:
            speak("what should i say ?")
            content = TakeCommand()
            to = "anjan.nwu@gmail.com"
            sendEmail(to, content)
            print("email has been sent")
            speak("email has been sent")

        except Exception as e:
            print("sorry sir, i am unable to send email")
            speak("sorry sir, i am unable to send email")

    def emailTorashmi():
        try:
            speak("what should i say ?")
            content = TakeCommand()
            to = "rasmyakter227@gmail.com"
            sendEmail(to, content)
            print("email has been sent")
            speak("email has been sent")

        except Exception as e:
            print("sorry sir, i am unable to send email")
            speak("sorry sir, i am unable to send email")

    def emailToNadeem():
        try:
            speak("what should i say ?")
            content = TakeCommand()
            to = "nadimsamratbd@gmail.com"
            sendEmail(to, content)
            print("email has been sent")
            speak("email has been sent")

        except Exception as e:
            print("sorry sir, i am unable to send email")
            speak("sorry sir, i am unable to send email")





    if __name__ == "__main__":
            wishme()
       # while True:
            query = TakeCommand().lower()

            # logic for exexuting task

            #wikipedia search
            if 'wikipedia' in query :
                speak('searching wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences = 2)
                speak("according to wikipedia ")
                print(results)
                speak(results)

            #google search
            elif "open google" in query:
                speak("sir, what should i search for ")
                search = TakeCommand()
                webbrowser.open(f"{search}")

            elif "search" in query:

                query = query.replace("search", "")
                speak("searching" + query)
                pywhatkit.search(query)

            #introduce
            elif 'hey david' in query:
                introduce()

            #open websites by calling
            elif 'open youtube' in query:
                speak("opening")
                webbrowser.open("www.youtube.com")

            elif 'open facebook' in query:
                speak("opening")
                webbrowser.open("www.facebook.com")

            elif "open instagram" in query:
                speak("opening")
                webbrowser.open("www.instagram.com")

            elif 'open stack overflow' in query:
                speak("opening")
                webbrowser.open("www.stackoverflow.com")

            elif 'open github' in query:
                speak("opening")
                webbrowser.open("www.github.com")

            #play music from desktop/Laptop
            elif 'play music' in query:
                music_directory = 'E:\\music'
                songs = os.listdir(music_directory)
                print(songs)
                speak("playing")
                os.startfile(os.path.join(music_directory, songs[0]))

            #Ask for current time
            elif 'the time' in query:
                stringTime = datetime.datetime.now().strftime('%I:%M %p')
                print(stringTime)
                speak(f"sir, the time is {stringTime}")

            # Ask for date today
            elif 'the date' in query:
                stringDate = datetime.datetime.now().strftime('%Y-%m-%d')
                print(stringDate)
                speak(f"sir, today is {stringDate}")

            #open softwares
            elif "open notepad" in query:
                npath = "C:\\windows\\system32\\notepad.exe"
                speak("opening")
                os.startfile(npath)

            elif "open chrome" in query:
                chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                speak("opening")
                os.startfile(chrome)

            elif "open code block" in query:
                path = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
                speak("opening")
                os.startfile(path)

            elif "open powerpoint" in query:
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                speak("opening")
                os.startfile(path)

            elif "open ms word" in query:
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                speak("opening")
                os.startfile(path)

            elif "open net beans" in query:
                path = "C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe"
                speak("opening")
                os.startfile(path)

            elif "open photo shop" in query:
                path = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
                speak("opening")
                os.startfile(path)

            elif "open excel" in query:
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                speak("opening")
                os.startfile(path)

            elif "open zoom" in query:
                path = "C:\\Users\\Anjan\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
                speak("opening")
                os.startfile(path)

            elif "open packet tracer" in query:
                path = "C:\\Program Files\\Cisco Packet Tracer 8.0.1\\bin\\PacketTracer.exe"
                speak("opening")
                os.startfile(path)

            elif "open pycharm" in query:
                path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe"
                speak("opening")
                os.startfile(path)




            elif "open command prompt" in query:
                speak("opening")
                os.system("start cmd")



            #Send Emails
            elif "email to anjan" in query:
                emailToAnjan()

            elif "email to nadeem" in query:
                emailToNadeem()

            elif "email to rashmi" in query:
                emailTorashmi()

            #Search ip address
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                print(ip)
                speak(f"your IP address is {ip}")


            #stop program
            elif "stop" in query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()

            else:
                print("Sorry, This command is unknown to me")
                speak("Sorry, This command is unknown to me")






window = Tk()
window.title("Voice Assistant")
window.geometry("500x470")
window.config(background="#5cfcff")
lable1 = Label(window, text="Voice Assistant", font="Arial 20 bold", fg='#00ff00', bg='black', justify="center")
lable1.pack()

image = ImageTk.PhotoImage(file='pic.jpg')
lable2 = Label(window)
lable2.place(x=0, y=141)
lable2.config(image=image)
startButton = Button(window, text="Start Program", width=20, justify="center", bg='#E9CFEB', command=start)
startButton.pack()
exitButton = Button(window, text="Close Program", width=20, justify="center", bg='#ffcccb', command=exit)
exitButton.pack()
window.mainloop()
