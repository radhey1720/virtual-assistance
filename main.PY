import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser
import smtplib
import pyaudio
from PIL import  ImageGrab # alwasys there is some difference between the importing syntax
#yaha par yeh bahut halka isleye hai kyunki isse abhi ham log use nahi kiye hai




engine = pyttsx3.init()  #its the syntax to start speech to text conversion
voices = engine.getProperty('voices') #its used to change text  to voice
# print(voices[1].id) # its used to get to listen the trail voice
engine.setProperty('voice', voices[0].id) # its the function to set the voice to particular type




def speak(audio):
    engine.say(audio) #say ke andar likhna hoga ki isko kya bolna hai
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")  # yaha par print mat lagana kyunki hame bulwana hai

    elif hour>=12 and hour<18: #it means if else
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  #iska matlab ham log function ko call kar rahe

    speak("I am your asistance sir. Please tell me how may I help you") #function isleye call karna hai kyunki baar baar use karna hai



def takeCommand():
    r = sr.Recognizer() #iska matlab start recognizing the speech
    with sr.Microphone() as source:  #iska matlab source of voice listening
        print("Listening...") # taki user ko pata chale ki asistance is listening
        r.pause_threshold = 1 # kuch gab de two words ke bech
        audio = r.listen(source)  #part of the above sr.microphone code

    try:   # we have to use try as we dont want to hang our program
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") # or here we can write "user said:",query  for simple understanding

    except Exception as e:
        # print(e) # error nahi dikhana hai hame    
        print("Say that again please...")  
        return "None"
    return query 


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hackerspider1720@gmail.com','Mnnit@156')
    server.sendmail('hackerspider1720@gmail.com', to, content)
    server.quit()

'''
JAB TAK HAM FUNCTION KO CALL NAHI KARENGE TAB TAK WOH HAMARA KAM NAHI KAREGA
OR JIS JAGAH CALL KARENGE HAM FUNCTION USS JAGAH WOH HAMARA KAAM KAREGA

'''


wishme() # yaha par hamne call kiya ki matlab ab tmhara kaam shuru hua hai # MATLAB START YAHA SE HO 
while True: # hamesa true raho for below conditions
        query = takeCommand().lower()  # hamne yaha par take command ko call kiya hai

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) # its particular syntax of wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")   

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")         


        elif 'play music' in query:
            musiclocation = "C:\\Users\\91876\\Desktop\\PHYTON\\PYTHON PROJECTS\\ARTIFICIAL INTELIGENCE\\SONGS"
            songs = os.listdir(musiclocation) # We have to write this to interact our command with our operating system # isme mention kiye hai ham apne words mai ki andar kya hai
            #print(songs)    
            os.startfile(os.path.join(musiclocation, songs[0])) # phele number wala song  automatically play kardega
            stop = input("enter q to stop the music:")
            if (stop == q ):
                break
            else:
                None


        ####3elif 'stop music' in query:
        ##3os.startfile(os.path.join(musiclocation, songs[0])) 
           ### break 

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the hour is {strTime}") # or this can be written as "sir,the hour is",strTime

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'mail to radhe' in query: # we can here also create a whole bunch of dictionary
            try:
                speak("What should I say in the message?")
                content = takeCommand() #koi command lene ke liye
                to = "krishnaradhey1720@gmail.com"    
                sendEmail(to, content) # function calling here
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend radhey bhai. I am not able to send this email")


        elif 'quit' or 'stop' in query:
            break           # break is used to exit the command

        elif 'open image saved in folder' in query:
            # Location of the image
          img = Image.open("C:\\Users\\91876\\Desktop\\PHYTON\\PYTHON PROJECTS\\ARTIFICIAL INTELIGENCE\\radhey.png")
          img.show()

        elif 'screenshot' in query:
           image = ImageGrab.grab() # it would not save the image anywhere
           image.show()

        elif 'write a note' in query:
            f = open("data.txt",'w') # here we can only write
            f.write('content')
            f.close()

        elif 'open note' in query:
            f = open('data.txt','r') # here we can only read
            text = f.read()
            print(text)
            f.close()      


        elif 'google search' in query:
            pass

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that your fine")  

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by radhey.")  

        elif "who are you" in query:
            speak("I am your virtual assistant created by radhey")

        elif 'shutdown' in query:
            speak("WAIT SIR ! Your system is on its way to shut down")
            os.system("shutdown /s /t 1")  #its part of import.os

        elif 'restart' in query:
            speak("WAIT SIR ! Your system is on its way to restart")    
            os.system("shutdown /r /t  1")

        elif "camera" in query or "take a photo" in query:
            pass

        elif 'start video' in query:
            pass

        elif 'delete folder' in query or 'delete file' in query:
            pass

        elif 'search for file' in query or 'search for folder' in query or 'search for program' in query:
            pass

        elif 'uninstall program' in query:
            pass

        elif 'set reminder' in query or 'notification' in query:
            pass

        elif 'organise' in query:
            speak("Sir i am doing the task for you....Please wait for a second!")
            
        while (True): #yaha par true ka phela T capital hai
            def createIfNotExist(folder):  #function defining to create these folders
                if not os.path.exists(folder): #yeh check karne ke liye hai ki folder exist or not
                    os.makedirs(folder)   # yaha par hame kuch return nahi karna hai

            def move(folderName, files): #apne aap create hai ham
                for file in files:  #koi kaam baar baar karne ke liye
                    os.replace(file, f"{folderName}") 


        
                files = os.listdir()
                files.remove("main.py")

                createIfNotExist('Images')  #function calling
                createIfNotExist('Docs')    #function calling
                createIfNotExist('Media')   #function calling
                createIfNotExist('Others')  #function calling

                imgExts = [".png", ".jpg", ".jpeg"]
                images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]  #these are the superset

                docExts = [".txt", ".docx", "doc", ".pdf"]
                docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


                mediaExts = [".mp4", ".mp3", ".flv"]
                medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

                others = []
                for file in files:
                     ext = os.path.splitext(file)[1].lower()
                     if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
                          others.append(file)

                move("Images", images) #baad mai apostrophe nahi lagana hai kyunki phel hi laga chuke hai ham
                move("Docs", docs)
                move("Media", medias)
                move("Others", others)

        break #ab yeh dark hogaya iska matlab iska use hai

        





        
  


