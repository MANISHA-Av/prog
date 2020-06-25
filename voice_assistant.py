import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser as wb
import os
import smtplib as s
engine = pyttsx3.init('sapi5')#sapi5 gives the voice
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
#print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    elif hour>=18 and hour<21:
        speak('good evening')
    else:
        speak('good night')
    
    speak('i am anshika...please tell me how may i help you!')
    

def takeCommand():#take commands using microphone
    r = sr.Recognizer() # to recognize the audio
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        #r.dynamic_energy_threshold=True
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said : {query}\n')
    except Exception as e:
        print(e)
        print('please say it again')
        return 'None'
    return query

def sendEmail(to,content):
    
    ob=s.SMTP('smtp.gmail.com',587)
    ob.ehlo()
    ob.starttls()
    ob.login('ishitaraj103@gmail.com','Thisismanisha@123')
    ob.sendmail("ishitaraj103@gmail.com",to,content)
    print('send successfully')
    ob.close()

if __name__=='__main__':
    #speak('manisha is a good girl')
    wishMe( )
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary('shehnaaz gill', sentences=12)
        
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('youtube is opening....')
            wb.open('youtube.com')
        elif 'open google' in query:
            speak('google is opening....')
            wb.open('google.com')
        elif 'open stackoverflow' in query:
            speak('stackoverflow is opening....')
            wb.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\manisha\\Desktop\\music'
            songs = os.listdir(music_dir)#list all the songs in the directory
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))#we can play random song by importing random module and by looping
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            #print('the time is :',strTime)
            speak(f'mam the time is {strTime}')
        elif 'open jupiter' in query:
            code_path='C:\\Users\\manisha\\anaconda3\\python.exe'
            os.startfile(code_path)
        elif'send email' in query:
            try:
                speak('what should i say:')
                content = takeCommand()
                to = 'ishitaraj103@gmail.com'
                sendEmail(to,content)
                speak('email has been sent..')
            except Exception as e:
                print(e)
                speak('sorry email can not be sent..')

        