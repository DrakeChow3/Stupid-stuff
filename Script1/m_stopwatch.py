#! python3
# A simple stopwatch program

import time,pyperclip

print('Press enter to start.Press Ctrl+C to end')
input()
print('Start')
startTime=time.time()
lastTime=startTime
number=1
context=''
while True:
    try:
        input()
        lastRep='{:.2f}'.format(round(time.time()-lastTime,2))
        totalRep='{:.2f}'.format(round(time.time()-startTime,2))
        out_put='Lap #%s %s %s' % (str(number).rjust(3) , lastRep.rjust(5) , totalRep.rjust(5))
        context+=out_put+'\n'
        print(out_put,end='')
        number+=1
        lastTime=time.time()
    except KeyboardInterrupt:
        break
pyperclip.copy(context)