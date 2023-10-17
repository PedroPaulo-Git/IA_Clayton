import speech_recognition as sr
import webbrowser
import openai
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


openai.api_key = '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'
url_default = 'https://www.youtube.com/results?search_query='
xpath_ytb_search = '//*[@id="thumbnail"]/yt-image/img'
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('Listening...')
        listener.energy_threshold = 2000 
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        
        if 'alexa' in command:
            print(command) 
           
            if 'play' in command:
                search_query = command.replace('alexa play','')
                search_query = search_query.replace('','+')
                url = url_default+search_query  

                print('abrindo o navegador...') 

                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(3)
            
                video_get_video = driver.find_element(By.XPATH,xpath_ytb_search)
                video_get_video.click()
                print (video_get_video)
                time.sleep(10) 
               
except sr.WaitTimeoutError:
    print("Tempo limite atingido, pare de ouvir.")
except sr.UnknownValueError:
    print("Não foi possível reconhecer o áudio.")
except sr.RequestError as e:
    print(f"Erro ao chamar o serviço de reconhecimento de fala: ")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    """   """
           
         