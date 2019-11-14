#! python3
#resizing thousands of images and adding a small logo watermark to the corner of each

import os,logging
from PIL import Image
logging.basicConfig(level=logging.CRITICAL,format=' %(asctime)s - %(levelname)s - %(message)s ')

SQUARE_fIT_SIZE=300
logo='catlogo.png'

os.makedirs('resizeImage',exist_ok=True)
imgLogo=Image.open(logo)
logoWid,logoHei=imgLogo.size
for i in os.listdir('.'):
    if i==logo:
        continue
    elif i.lower().endswith(('.png','.jpg','.gif','.bmp')):
        imageObj=Image.open(i)
        width,height=imageObj.size
        if width > SQUARE_fIT_SIZE or height > SQUARE_fIT_SIZE:
            if width>height:
                height=int((SQUARE_fIT_SIZE/width)*height)
                width=SQUARE_fIT_SIZE
            else:
                width=int((SQUARE_fIT_SIZE/height)*width)
                height=SQUARE_fIT_SIZE
        if logoWid>width and logoHei>height:
            if logoWid > logoHei:
                logoHei=int((width*0.3/logoWid)*logoHei)
                logoWid=int(width*0.3)
            else:
                logoWid=int((height*0.3/logoHei)*logoWid)
                logoHei=int(height*0.3)
        pasteLogo=imgLogo.resize((logoWid,logoHei))
        imageObj=imageObj.resize((width,height))
        imageObj.paste(pasteLogo,(width-logoWid,height-logoHei),pasteLogo)
        imageObj.save(os.path.join('resizeImage',i))