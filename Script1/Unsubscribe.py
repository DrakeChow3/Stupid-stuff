#! python3
# a program that scans through your email account, finds all 
# the unsubscribe links in all your emails, and automatically opens them in a browsers

#I stopped writing the program midway because google add a unsubcribe button on top of the header

import pyzmail,imapclient,imaplib,pprint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
imaplib._MAXLINE=100000000

#log in the gmail and fetch all the email
imapObj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
imapObj.login('severbreaker23@gmail.com','megaman123')
imapObj.select_folder('INBOX',readonly=True)
UIDs=imapObj.search('ALL')
#TODO:go through each email and find the word 'unsubscribe'
# for id in UIDs:
for i in range(1675,1690):
    rawMess=imapObj.fetch([i],['BODY[]','FLAGS'])
    pyzObj=pyzmail.PyzMessage.factory(rawMess[i][b'BODY[]'])
    file=open('page'+str(i)+'.html','w',encoding='utf8')
    file.write(pyzObj.html_part.get_payload().decode(pyzObj.text_part.charset))
    file.close()
#TODO:open the 'unsubcribe' page in the new tab