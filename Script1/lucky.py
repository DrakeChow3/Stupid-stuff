#! python3
# type a search term on the command line and have 
# my computer automatically open a browser with all the top search results in new tabs


#SELENIUM WITH HEADLESS FIREFOX SUCCCEED !!!!!!!!!!!!!!!!!!!!!!!

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import bs4,sys,webbrowser

# print('Googling.....')
# options=Options()
# options.headless=True
# url='https://www.google.com/search?q='+'_'.join(sys.argv[1:])
# try:
#     browser=webdriver.Firefox(options=options)
#     browser.get(url)
#     parse=bs4.BeautifulSoup(browser.page_source,features="html.parser")
#     linkRequest=parse.select('.r>a')
#     total_count=min(5,len(linkRequest))
#     for i in range(total_count):
#         # webbrowser.open(linkRequest[i].get('href'))
#         print(linkRequest[i].get('href'))
#     browser.quit()
# except Exception as err:
#     print('An error has occurred '+str(err))