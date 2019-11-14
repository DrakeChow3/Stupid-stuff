#! python3
# create images for custom seating cards for your guests
# generate an image file with the guest name and some flowery decoration
#It actually work,whao,but ugly though :((((

import os,logging
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.WARNING,format=' %(asctime)s - %(levelname)s - %(message)s ')

#a function to shrink down the image for the invitation card
def shrinkImg(img,w,h):
    #TODO:if the img width and height bigger than width and height of the remaining blank space
    width,height=img.size
    if width > w or height >h:
        if width > height:
            height=int((w*0.75/width)*height)
            width=int(0.75*w)
        else:
            width=int((h*0.75/height)*width)
            height=int(0.75*h)
    return img.resize((width,height))
    #return the ImageObj which has been shrank down

os.makedirs('PictureInvi',exist_ok=True)
guessFile='guests.txt'  #Specify the guest
arialFont = ImageFont.truetype('arial.ttf', 30) #Specify font text

#Open the guest text file
guestText=open(guessFile,'r')
#Find all guests and images with the number of guest given
totalGuests=[]
totalImage=[]
totalImage_number=0
for guest in guestText.readlines():
    totalImage_number+=1
    totalGuests.append(guest.strip())
count=0
for i in os.listdir('.'):
    if count == totalImage_number:
        break
    if i.lower().endswith(('.jpg','.png')):
        totalImage.append(i)
        count+=1
logging.critical('Guest: '+str(totalGuests))
logging.critical('Images: '+str(totalImage))
#Loop through each guest and create their own invitation card

img_count=0
for n in range(len(totalGuests)):
    #create an image and add the guest's name with style
    img=Image.new('RGBA',(290,362),'white') #the card is 288x360(4x5 inch card),i add morev pixels for black rectangle
    draw=ImageDraw.Draw(img)
    width,height=draw.textsize(totalGuests[n],arialFont)
    draw.text((int(145-width/2),20),totalGuests[n],fill='black',font=arialFont)
    #TODO:shrink down the image to fit the card and add the image
    imgObj=Image.open(totalImage[img_count])
    imgObj=shrinkImg(imgObj,360,288-height-20)
    w,h=imgObj.size
    img.paste(imgObj,(int(145-w/2),288-h))
    img_count +=1
    #TODO:add black rectangle at the edge
    draw.line([(0,0),(289,0),(289,361),(0,361),(0,0)],fill='red')
    img.save(os.path.join('PictureInvi',totalGuests[n]+'.png'))