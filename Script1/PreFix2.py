#! python3
#write a program that can insert gaps into numbered files so that a new file can be added.

import os,shutil,re


def GapFile(prefix,number,folder):
    folder=os.path.abspath(folder) #make sure the path is absolute
    #Create a regex for the file to be gapped
    reGex=re.compile(r"""^("""+prefix+""") #prefix the the file to be found
                     00     #the double zero in the name
                     ("""+number+""") #number of the file to be gapped
                     (.*?)$ #Whatever come after the number
                     """,re.VERBOSE)
    number=int(number)
    for filename in os.listdir(folder):
        mo=reGex.search(filename)
        if mo==None:
            continue
        fend=mo.group(3)
        next_file=prefix+'00'+str(number+1)+fend
        if os.path.exists(os.path.join(folder,next_file)):
            CreateGap(prefix,number+1,fend,folder)
        shutil.move(os.path.join(folder,filename),os.path.join(folder,next_file))
            
def CreateGap(fprefix,score,fend,folder):
    start=score+1
    while True:
        if os.path.exists(os.path.join(folder,fprefix+'00'+str(start)+fend)):
            start+=1
            continue
        else:
            break
    for i in range(score,start):
        _font=os.path.join(folder,fprefix+'00'+str(score)+fend)
        _end=os.path.join(folder,fprefix+'00'+str(score+1)+fend)
        shutil.move(_font,_end)
        
#GapFile('spam','4','Superfolder')