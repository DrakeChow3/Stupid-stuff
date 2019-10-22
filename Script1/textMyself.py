#! python3
# Defines the textmyself() function that texts a message
# passed to it as a string.
#this suck
#preset value
sID='AC469d7ee82e0e734b2826288772503477'
aut_Token='d678f64c6947b93610e276df55cf94b9'
twi_Number='+15005550006'
my_Num='+0901304870'

from twilio.rest import Client

def textmyself():
    try:
        client=Client(sID,aut_Token)
        call=client.messages.create(body='Custom text',from_=twi_Number,to=my_Num)  
    except Exception as err:
        print('Error '+str(err))
    
textmyself()
