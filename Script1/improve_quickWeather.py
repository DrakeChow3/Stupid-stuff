#! python3
#Fetching Current Weather Data

import json,bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.headless=True
url='http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=b2e92b0c9bbd50f1fb63c2b3957dcd86'
wb=webdriver.Firefox(options=options)
wb.get(url)
all_content=bs4.BeautifulSoup(wb.page_source,features='html.parser')
j_content=all_content.select('div')
content=json.loads(str(j_content[0].getText()))
print('Current weather in London,UK')
print(content['weather'][0]['main']+'-'+content['weather'][0]['description'])
wb.close()

#im too lazy for this part
#improved
#else if statement if it is raining today.The program will send a text for me to take an umbrella