#! python3
# using command line to send email
#This program did connect to gmail you have to sign in everytime with your gmail because it not
# uses any data on your own firefox
#kind of annoying though,so i stop there and more on another program

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os,sys,bs4,webbrowser

email=sys.argv[1]
content_text=" ".join(sys.argv[2:])
options=Options()
options.headless=True
try:
    browser=webdriver.Firefox(options=options)
    print('Going into gmail.....')
    browser.get('https://mail.google.com')
    print('Creating letter...')
    print(browser.page_source)
    compose=browser.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
    compose.click()
    receiver=browser.find_element_by_id('pj')
    receiver.send_keys(email)
    content=browser.find_element_by_id(':q6')
    content.send_keys(content_text)
    content.submit()
    print('Done')
except Exception as err:
    print('Cant send letter because '+str(err))