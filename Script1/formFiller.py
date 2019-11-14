#! python3
# using pyautogui to fill out form

import pyautogui,time,logging
logging.basicConfig(level=logging.CRITICAL,format=' %(asctime)s - %(levelname)s - %(message)s ')

nameField=(435,531)
submitButton=(427,622)
submitBtncolor=(196,177,232)
submitAnotherlink=(429,410)
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand','robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet',
            'robocop': 4,'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
             'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money','robocop': 5,
              'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

pyautogui.PAUSE=0.5
for person in formData:
    print('PAUSE THE PROGRAM 5 SECOND BEFORE STARTING')
    time.sleep(5)
    #Move to the first field:name field
    pyautogui.click(nameField[0],nameField[1])
    pyautogui.typewrite(person['name']+'\t',0.05)
    #Move to fear field
    pyautogui.typewrite(person['fear']+'\t',0.05)
    #To the wizard field
    logging.critical(person['source'])
    if person['source'] == 'wand':
        pyautogui.typewrite(['down','enter','tab'],0.2)
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down','down','enter','tab'],0.2)
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down','down','down','enter','tab'],0.2)   
    elif person['source'] == 'money':
        pyautogui.typewrite(['down','down','down','down','enter','tab'],0.2)
    #to the robocop field:
    logging.critical(str(person['robocop']))
    if person['robocop'] == 1:
        pyautogui.typewrite([' ','tab'],0.2)
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right','tab'],0.2)
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right','right','tab'],0.2)
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right','right','right','tab'],0.2)
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right','right','right','right','tab'],0.2)
    #to the comment field
    pyautogui.typewrite(person['comments']+'\t'+'\t',0.05)
    #to the submit button
    pyautogui.press('enter')
    print('clicked submit')
    #Wait for the new page
    time.sleep(4)
    pyautogui.click(submitAnotherlink[0],submitAnotherlink[1])