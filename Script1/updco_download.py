#! python3
# check if the comic is updated and download it

import bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#open or create the file in read mode and append mode
file=open('xkcd.txt','a+')
#access the headless webrowser
options=Options()
options.headless=True
try:
    wb=webdriver.Firefox(options=options)
    wb.get('https://xkcd.com')
    page=bs4.BeautifulSoup(wb.page_source,features='html.parser')
    content=page.select('div[id="comic"]>img')
    if content==[]:
        pass
    else:
        url=content[0].get('src')+'\n'
        if url not in file.readlines():
            file.append(url)
            #This is the part where i download the comic,but i really dont want to
except Exception as err:
    pass
file.close()