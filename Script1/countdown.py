#! python3
# make a stop watch program

import time,subprocess

time_left=5
while time_left > 0:
    print('Time left '+str(time_left))
    time.sleep(1)
    time_left-=1
subprocess.Popen(['start','alarm.wav'],shell=True)