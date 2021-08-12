import datetime
import pyttsx3
import pywhatkit
import speech_recognition as mr
import weather_forecast as wf
import wikipedia
import webbrowser
import os
from tkinter import *
root=Tk()

root.title("VIRTUAL AI")
root.geometry('360x640')
bg = PhotoImage(file = "mani.png")
label1 = Label(root, image = bg) 
label1.place(x = 0, y = 0) 


listener =mr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with mr.Microphone() as source:
            print('Hello MANI.....')
            talk('hello MANI ')
            voice = listener.listen(source)
            command =listener.recognize_google(voice)
            command =command.lower()
            if'mani' in command:
                command = command.replace('mani', '')
                print(command)


    except:

        pass
    return command

def run_mani():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing  ' + song)
        pywhatkit.playonyt(song)
    elif 'time now' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'i got fever' in command:
        print('The average normal body temperature is 98.6°F (37°C). Body temperature above 100°F is usually classified as fever.')
        talk('The average normal body temperature is 98.6°F (37°C). Body temperature above 100°F is usually classified as fever.')
    elif 'i am feeling cold' in command:
        print('drink some hot water')
        talk('sir please take care about your health and drink some hot water')

    elif 'weather today' in command:
        print(wf.forecast(place = "guntur"))
        talk('weather result are shown on screen')
        from time import sleep
        sleep(10)

    elif 'what is my name' in command:
        print('MANI')
        talk('your sweet name is mani')

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        about = wikipedia.summary(thing,1)
        print(about)
        talk(about)
    elif 'hello' in command:
        print('hello mani')
        talk('hello mani i am happy to hear u! how can i help you ?')

    elif 'okay' in command:
        print('thank you')
        talk('thank you')
    elif 'ok' in command:
        print('thank you ')
        talk('thank you ')
    elif 'show note' in command:
        f = open("mani.txt", "r")
        print(f.read())

        talk('you re note has been displayed on screen')
    elif 'increase volume'in command:
        from winsystem import Volume
        volume = Volume.Volume_control().SetVolUp(10)
        talk('your system volume has been increased by 10%')
        print('your system volume has been increased by 10%')
    elif 'decrease volume' in command:
        from winsystem import Volume
        volume = Volume.Volume_control().SetVolDown(10)
        print('your volume has been decreased')
        talk('your volume has been decreased by 10%')
    elif 'increase brightness' in command:
        from screen_brightness_control.windows import set_brightness
        bright = set_brightness(100)
        print('your system brightness has been increased to 100%')
        talk('your system brightness has been increased to 100%')

    elif 'decrease brightness' in command:
        from screen_brightness_control.windows import set_brightness
        bright = set_brightness(50)
        print('your system brightness has been set to 50%')
        talk('your system brightness has been set to 50%')
    elif 'write note' in command:
        f = open("mani.txt", "a")
        n = command.replace('write note', '')
        f.write(n+'\n')
        f.close()
    elif 'show my contact list' in command:
        f = open("text.txt", "r")
        print(f.read())
        talk('your contactslist has been displayed')
    elif 'add contact' in command:
        f = open("text.txt", "a")
        n = command.replace('add contact', '')
        f.write(n+'\n')
        f.close()
    elif 'open e drive' in command:
       os.startfile("E://")
       talk('disk has been shown')
    elif 'open d drive' in command:
       os.startfile("D://")
       talk('disk has been shown')
    elif 'open chrome' in command:
       os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
       talk('your chrome browser has been opened')
    elif 'open whatsapp' in command:
        os.system("start \"\" https://web.whatsapp.com/")
        talk('whatsapp has been opened')
    elif 'open amazon prime' in command:
        os.system("start \"\" https://www.primevideo.com/")
        talk('amazon prime has been opened')
    elif 'open contacts' in command:
        os.system("start \"\" https://contacts.google.com/")
        talk('contacts has been opened')
    elif 'open instagram' in command:
        os.system("start \"\" https://www.instagram.com/")
        talk('instagram has been opened')
    elif "locate" in command:
        command = command.replace("locate ", "")
        location = command
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.com/maps/search/" + location + "")
    elif 'show location' in command:
        os.system("start \"\" https://www.google.com/maps/")
        talk('Your location has beenshown')

    else:
        talk('can please repeat the command.')
        run_mani()

  
b1=Button(root,text='SPEAK',width=5, bg="black", fg="blue",font=('Impact', 20), command=run_mani) 
b1.pack()  
b1.grid(column=100, row=0)
b1.place(relx=.5,rely=.2,anchor= "c") 
root.mainloop() 


