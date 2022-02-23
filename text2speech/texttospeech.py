# this function will convert text into audio file 
import pyttsx3
  


def t2s(voice , text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    male=voices[0].id
    female=voices[1].id

    if voice=="female":
        engine.setProperty('voice', female)
    if voice=="male":
        engine.setProperty('voice', male)

    engine.save_to_file(text, 'download/voice.mp3')
    engine.runAndWait()

    return 

#t2s("female" , "hello ")  test data
