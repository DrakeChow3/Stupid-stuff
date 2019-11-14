#! python3
# a program to move the mouse cursor every 10 seconds

from random import choice
import pyautogui,time

class moveMouse():
    def __init__(self,time=10):
        self.time=time
    
    def move(self):
        s=0
        while s<self.time:
            print(f"Time: {s} ")
            try:
                if s!=self.time-1:
                    s+=1
                    time.sleep(1)
                else:
                    pyautogui.moveRel(choice([-1,1]),choice([-1,1]),duration=0.25)
                    s=0
            except KeyboardInterrupt:
                print('Done')
                break

testing=moveMouse()
testing.move()