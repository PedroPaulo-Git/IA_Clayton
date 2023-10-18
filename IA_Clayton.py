import speech_recognition as sr
import openai
import psycopg2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#connection BD >>>
conn = psycopg2.connect(
dbname ='IA_ClaytonBD',
user= 'postgres',
password='123',
host='localhost'
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM phrases_english")

rows = cursor.fetchall()
for row in rows:
    print(row)
    cursor.close()
    conn.close()




#openai.api_key = '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'
url_default = 'https://www.youtube.com/results?search_query='
xpath_ytb_search = '//*[@id="video-title"]/yt-formatted-string'
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('Listening...')
        listener.energy_threshold = 2000 
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        chrome_service = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        chrome_service.command_line_args()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        options.add_experimental_option('useAutomationExtension',True)
        options.add_argument('--remote-debugging-port=8989')
        options.add_argument(r'--user-data-dir=C:\Users\inesg\AppData\Local\Google\Chrome\User_Data')

        
        if 'alexa' in command:
            print(command) 
           












            if 'play' in command:
                search_query = command.replace('alexa play','')
                search_query = search_query.replace('','+')
                url = url_default+search_query  

                print('opening Chrome...') 
                driver = webdriver.Chrome(service=chrome_service,options=options)
                driver.get(url)
                time.sleep(2)
            
                video_get_video = driver.find_element(By.XPATH,xpath_ytb_search)
                while True:
                    try:
                        content_element = driver.find_element(By.XPATH,'//*[@id="dismissible"]')
                        title = content_element.text
                        video_get_video.click()
                        print('video found')
                        
                        time.sleep(15)

                        ad = driver.find_element(By.XPATH,'//*[@id="ad-text:1a"]') 
                        if ad:
                            ad.click()
                            print('ad skipped')
                        else:
                            print('ad dont found')
                        break
                    except Exception as e:
                     print(f'error in > {e}')
                     #//*[@id="ad-text:1a"]
                    break
               
                chromeopen = False
                while True:
                    try:
                        windowsOpen = driver.window_handles
                        if len(windowsOpen) >= 1:
                            if not chromeopen: 
                                print(f"open tabs: {len(windowsOpen)}")
                                chromeopen = True
                    except Exception as e:
                        print(f'Erro: {e}')
                        print('Chrome closed')
                        driver.quit() 
                        break
                    else:
                         if len(windowsOpen) < 1: 
                            print (len(windowsOpen))
                            
                  
               
except sr.WaitTimeoutError:
    print("Tempo limite atingido, pare de ouvir.")
except sr.UnknownValueError:
    print("Não foi possível reconhecer o áudio.")
except sr.RequestError as e:
    print(f"Erro ao chamar o serviço de reconhecimento de fala: ")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    """   """
           
         