import getsmscode
import time

api = getsmscode.getsmscode('your_username', 'your token') #username = email, token can be found on the homepage @ getsmscode.com
print('My balance is: ' + str(api.get_balance())) #print balance

#get a chinese (+86) number for Telegram
number = api.get_number(10, 'cn')
print('Requested phone number is +' + str(number))
#loop until an sms received
print('Waiting code...')
sms = api.get_sms(number, 10, 'cn')
while not sms:
    time.sleep(5)
    sms = api.get_sms(number, 10, 'cn')
#print the received sms
print('Got sms:', sms)
print('')

#get a brazil (+55) number for Telegram
number = api.get_number(10, 'br')
print('Requested phone number is +' + str(number))
#loop until an sms received
print('Waiting code...')
sms = api.get_sms(number, 10, 'br')
while not sms:
    time.sleep(5)
    sms = api.get_sms(number, 10, 'br')
#print the received sms
print('Got sms:', sms)
