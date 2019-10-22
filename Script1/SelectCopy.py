#! python3
#a program that walks through a folder tree and searches for files with a certain file 
#extension (such as .pdf or .jpg).Copy these files from whatever location they are in to a new folder.

import os,shutil

def SearchFolder(extension,folder,new_fol):
    folder=os.path.abspath(folder) #get the absolute path of the folder to search
    new_fol=os.path.abspath(new_fol) #get the absolute path of the new folder
    for foldername,subfolder,filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.'+extension):
                print('Adding '+filename+' to '+new_fol)
                shutil.move(os.path.join(foldername,filename),new_fol)

#SearchFolder('pdf','Cong nghe phan mem','ahaha')