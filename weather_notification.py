from plyer import notification
from bs4 import BeautifulSoup as bs
import requests, time

try:
    file = open('city.txt', 'r')
    for city in file:
        print(f'Weather Notification 0.0.1\nCidade atual: {city}')
        
        while True:
            page = requests.get(f'https://www.tempo.com/{city}.htm')
            soup = bs(page.content, 'html.parser')

            temperature = soup.find('span', class_='dato-temperatura changeUnitT').get_text()
            thermal_sensation = soup.find('span', class_='txt-strng').get_text()
                        
            notification_title = 'CLIMA'  
            notification_message = (f'Temperatura atual em {city.title()}:{temperature}\nSensação térmica: {thermal_sensation}')  
            notification_app = 'CLIMA'
                
            notification.notify(  
                title = notification_title,  
                message = notification_message,
                app_name = notification_app,
                app_icon = 'icons/bolt-solid.ico',  
                timeout = 5,
                toast = False
                )
            time.sleep(30) # time in seconds
            
    file.close()
except FileNotFoundError:
    city = input('Digite sua cidade: ')
    def checkcity(str):
        flag_l = False
        flag_n = False
        
        for i in str:
            if i.isalpha():
                flag_l = True
            if i.isdigit():
                flag_n = True   
        return flag_l and flag_n
     
    if checkcity(city) == True:
        print('Digite apenas números!')
    else:         
        file = open('city.txt', 'w')
        for i in range(0, len(city), 1):
                if (city[i] == ' '):
                    city = city.replace(city[i], '-')
        file.write(city)
        file.close()