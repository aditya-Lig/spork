import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import smtplib
import datetime
import wikipedia
import winsound
import schedule
import time

a =('calix')



freq = 2500
duration = 80

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        winsound.Beep(freq, duration)
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en')
            print('you said :'+ query + '\n')

        except Exception as e :   
            print(e)
            print("Say that again please...")  
            return "None"
        return query     
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rontprince@gmail.com', 'Prince@333')
    server.sendmail('rontprince@gmail.com', to, f"Subject: Testing\n{content}",)
    server.close()

def fixMeeting():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rontprince@gmail.com', 'Prince@333')
    server.sendmail('rontprince@gmail.com', to, f"Subject: Testing\n{content}",)
    server.close()


if __name__=="__main__":
    
    while True:
        query = takeCommand().lower()
    #NORMAL CONVERSATIONS AS COMMAND
        if f'hello {a}' in query or 'hi' in query or 'hello there' in query or 'hi there' in query:
            speak(" Hello Sir,how may i help you")
            print(speak)

        elif 'how are you' in query:
            speak("sir, i am always fine")

        elif 'who i am' in query or 'who am i' in query:
            speak("sir, you are Aditya Kumar Mahalik and my creator.")
        elif 'what are you doing' in query:
            speak("sir i am doing your work") 

        elif 'what is your name' in query:
            speak(" My name is CALIX and i am your personal AI")          

        elif 'what is the time right now' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")        

    #PC INTERACTIONS AS COMMAND 
        elif 'google' in query:
            speak ('opening google')
            results = webbrowser.open("google.com")
            speak(results) 
        
        elif 'youtube' in query:
            speak ('opening youtube')
            results = webbrowser.open("youtube.com")
            speak(results)            
        

        elif 'open opera gx' in query:
            speak('opening opera gx')
            operagxPath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"      
            results = os.startfile(operagxPath)
            speak(results)
        
        elif 'open pubg' in query:
            speak('opening pubg')
            gameloopPath = "D:\\Program Files\\TxGameAssistant\\AppMarket\\AppMarket.exe"      
            results = os.startfile(gameloopPath)
            speak(results)   
        elif 'open vs code' in query:
            speak('opening vs code')
            vscodePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            results = os.startfile(vscodePath)
            speak(results)

        elif 'open ummy video downloader' in query:
            speak('opening ummy video downloader')
            uvdPath= "C:\\Users\\hp\\AppData\\Local\\UmmyVideoDownloader\\UmmyVideoDownloader.exe" 
            results = os.startfile(uvdPath)
            speak(results)    

        elif 'wikipedia' in query:
            speak ('searching in wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia") 
            print(results)
            speak(results)   


        elif 'play music' in query:
            speak('playing music')
            music_dir = 'D:\\Albums'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'shutdown computer' in query:
            speak('shuting down computer in 10 seconds')
            os.system("shutdown /s /t 10")


        elif 'restart computer' in query:
            speak('restating computer in 10 seconds')
            os.system("shutdown /r /t 10") 

        elif 'log off computer' in query:
            speak('logging off computer in 10 seconds')
            os.system('shutdown /l /t 10')
              
        elif 'cancel shutdown' in query:
            speak('ok sir')
            os.system('shutdown /a')      
           
        elif 'stop listening' in query:
            speak('ok sir')
            break    
        
    # SEND A EMAIL

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "nilakantha603@gmail.com"
                sendEmail(to, content)
                speak("sir! your email has been sent")
            except Exception as e: 
                print(e)
                speak("sorry sir, i am not able to sent your email")    

    # ARRANGE A MEETING
        
        elif 'fix a meeting' in query:
            speak("sir, what should i say?")
            to = ["adityakumarmahalik@gmail.com","niteshp282000@gmail.com","tanmaymakode76@gmail.com"]
            content = takeCommand()
            try:
                schedule.every(10).seconds.do(fixMeeting)
                while 1:
                    schedule.run_pending()
                    time.sleep(1)
            except Exception as e:
                print(e)
                speak("sorry sir! I am not able to fix the meeting")        

 

    #COVID19 CHECKER

        elif 'open covid-19 checker' in query:
            speak('opening covid-19 checker')
            print("are you experiencing any of the following symptoms?")
            speak('are you experiencing any of the following symptoms?')
            print(" cough \n fever \n difficulty in breathing \n none of the above")

            while True:
                choices = takeCommand()

                if choices == 'cough' or choices == 'fever' or choices == 'difficulty in breathing':
                    print("have you ever had any of the following?")
                    speak("have you ever had any of the following?")
                    print(" diabetes \n hypertension \n lung disease \n heart disease \n none of the above")
                

                elif choices == 'diabetes' or choices == 'hypertension' or choices == 'lung disease' or choices == 'heart disease':
                    print("have you traveled anywhere internationally in the 28-45 days?")
                    speak("have you traveled anywhere internationally in the 28-45 days?")
                    print(" yes \n no")

                elif choices == 'yes':
                    print("your infection risk is moderate.Please remember to stay quarantined for 14 days after your travel.While you are feeling absolutely healthy and kindly inform to nearest hospital. Thank you for this assessment.")
                    speak("your infection risk is moderate.Please remember to stay quarantined for 14 days after your travel.While you are feeling absolutely healthy and kindly inform to nearest hospital. Thank you for this assessment.")

                elif choices == 'no':
                    print("your symptoms are saying that you have normal fever and for more safty you need to self quaramtine for 14 days and take a pill of paracetamol.Thank you for this assessment.")
                    speak("your symptoms are saying that you have normal fever and for more safty you need to self quaramtine for 14 days and take a pill of paracetamol.Thank you for this assessment.")
                
                elif choices == 'non of the above':
                    print("have you traveled anywhere internationally in the 28-45 days")
                    speak("have you traveled anywhere internationally in the 28-45 days")
                    print(" yes \n no")

                # elif choices == 'which of the following to you?':
                #     print("have you recently interacted with positive covid-19 person?")
                #     speak("have you recently interacted with positive covid-19 person?")
                #     print(" yes \n no")    

                
                elif choices =='close checker':
                    speak("closing checker")
                    break  


        #PUTTING INTERNET SPEED CHECKER
                  
