import speech_recognition as sr

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('Listening...')
        listener.energy_threshold = 5000 
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        
        if 'clayton' in command:
            print(command)
            
except:
    pass
    print('Mic error')