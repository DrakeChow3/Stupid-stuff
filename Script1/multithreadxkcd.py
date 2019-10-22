#! python3
# download xkcd comic with threading

import os,threading,bs4,requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

os.makedirs('ComicXKCD',exist_ok=True)
def downloadxkcd(startnumb,endnumb):
    options=Options()
    options.headless=True
    wb=webdriver.Firefox(options=options)
    for comic_num in range(startnumb,endnumb+1):
        print('Downloading page http://xkcd.com/%s' %(comic_num))
        wb.get('http://xkcd.com/%s' %(comic_num))
        page=bs4.BeautifulSoup(wb.page_source,features='html.parser')
        content=page.select('div[id="comic"]>img')
        if content== []:
            print('No comic found')
        else:
            d_comic=content[0].get('src')
            print('Downloading comic '+d_comic)
            comic_page=requests.get(d_comic)
            comic_page.raise_for_status()
            imageFile=open(os.path.join('ComicXKCD',os.path.basename(d_comic)),'w')
            for chunk in comic_page.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
ThreadNums=[]            
for thread_num in range(0,1400,100):
    ThreadNum=threading.Thread(target=downloadxkcd,args=(thread_num,thread_num+99))
    ThreadNums.append(ThreadNum)
    ThreadNum.start()

for thread in ThreadNums:
    thread.join()
print('Done')