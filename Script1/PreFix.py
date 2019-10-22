#! python3
#Write a program that finds all files 
#with a given prefix in a single folder and locates any gaps in the numbering
#Have the program rename all the later files to close this gap.

import os,shutil,re

def FindFile(prefix,folder):
    #get the absolute path of the folder
    folder=os.path.abspath(folder)
    #create regular expression depend on the prefix    
    #First regex:Chi lay toi phan tram
    #Second regex:Chi co 3 don vi,2 don vi dau luon luon la so 0
    reGex_2=re.compile(r"""^("""+prefix+""") #the prefix
        00                                 #2 so khong o dau
        (\d+)                             #the number
        (.*?)$                           #every word after the number         
        """,re.VERBOSE)
    #Chi lay reGex_2 vi reGex_1 xay ra qua nhieu if
    while True:
        check=1
        for filename in os.listdir(folder):
            mo=reGex_2.search(filename)
            if mo==None:
                continue
            fprefix=mo.group(1)
            number=int(mo.group(2))
            if number==1:
                continue
            pre_file=fprefix+'00'+str(number-1)+mo.group(3)
            if not os.path.exists(os.path.join(folder,pre_file)):
                check=0
                _font=os.path.join(folder,filename)
                _end=os.path.join(folder,pre_file)
                print('Changing name '+_font+' to '+_end)
                shutil.move(_font,_end)     
        if check ==1:
            break
FindFile('spam','Superfolder')