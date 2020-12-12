#check a username and PIN code

database = [
    ['albert','1234'],
    ['rowan','2249'],
    ['claire','4444'],
    ['smith', '8987']
    ]

username = input('Username: ')
pin = input('PIN: ')

if [username,pin] in database:
    print('Access Granted')
else: print('Access Denied')

