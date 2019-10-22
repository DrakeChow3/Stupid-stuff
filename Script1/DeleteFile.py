#! python3
# deleting file which is too large(in this case >5mb hehe)

import os,send2trash

def Delfile(folder):
    #get the absolute path of the folder
    folder=os.path.abspath(folder)
    for foldername,subfolder,filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername,filename)) > 5000:
                print('Sending '+filename+ ' to trash')
                send2trash.send2trash(filename)
                
#Delfile('ServletSlideDemo')