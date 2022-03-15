import pywhatkit
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
no = input('Enter Mobile No of Receiver with country code: ')
msg = input('Enter Message you wanna send : ')
hr = int(input('Enter hour : '))
min = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(no,msg,hr,min)