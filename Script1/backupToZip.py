#! python 3
# a program to back up data to a zip file

import zipfile,os

def backupToZip(folder):
    folder=os.path.abspath(folder) #make sure the path is absolute
    #find the name for the zip file
    number = 1
    while True:
        baseName=os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(baseName):
            break
        number+=1
    #create the zip file
    print('Creating the zip file'+baseName)
    thezip=zipfile.ZipFile(baseName,'w')
    #prefix of all the zip file
    prefix=os.path.basename(folder)
    #include all the file in the folder and subfolder to the zip file
    for foldername,subfolder,filenames in os.walk(folder):
        print('Adding file in '+foldername)
        #writing each folder into the zip file
        thezip.write(foldername)
        #loop through each file in filenames and add it to the correct folder
        for filename in filenames:
            #check if the file is another zip file,just in case
            if filename.startswith(prefix) and filename.endswith('.zip'):
                continue
            thezip.write(os.path.join(foldername,filename))
    thezip.close()

#backupToZip('D:\java\ServletSlideDemo\ServletSlideDemo\DemoBasicServlet')
