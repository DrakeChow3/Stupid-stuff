#! python3
# constantly displays the x- and y-coordinates of the mouse cursor as you move it around.

import pyautogui
#fail safe
pyautogui.PAUSE=1
pyautogui.FAILSAFE= True
print('Crtl + C to quit')
while True:
    try:
        x,y=pyautogui.position()
        text=('X:'+str(x).rjust(4)+' ,Y:'+str(y).rjust(4))
        screenshot=pyautogui.screenshot().getpixel((x,y))
        text+=(' ,GRB:'+str(screenshot[0]).rjust(3))
        text+=(','+str(screenshot[1]).rjust(3))
        text+=(','+str(screenshot[2]).rjust(3))
        print(text,end='')
        print('\b'*len(text),end='',flush=True)
    except KeyboardInterrupt as err:
        print('Out of the loop')
        break