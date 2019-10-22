#! python3
# print the absolute path of any photo folders to the screen.

import os,logging
from PIL import Image
logging.basicConfig(level=logging.WARNING,format=' %(asctime)s - %(levelname)s - %(message)s ')

for foldername,subfolder,filenames in os.walk('D:\MyPythonScipts'):
    photoFile=0
    nonphotoFile=0
    logging.warning('CURRENT FOLDER %s' %(foldername))
    for filename in filenames:
        logging.warning('Current filename %s ' %(filename))
        try:
            if not filename.lower().endswith(('.jpg','.png','.gif')):
                nonphotoFile += 1
                continue
            imgObj=Image.open(filename)
            width,height= imgObj.size
            if width > 10 and height >10:
                photoFile +=1
            else:
                nonphotoFile +=1
        except Exception:
            logging.critical('Cant open file %s ' %(filename))
    logging.critical('photo file %d - non photo file %s' %(photoFile,nonphotoFile))
    if photoFile >nonphotoFile:
        print('Photo folder :'+foldername)