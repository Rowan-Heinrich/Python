#A Simple Database using get()

people = {
    'Alice':{'phone':'2431','addr':'Foo Drive 23'},
    'Beth':{'phone':'9102','addr':'Bar Street 42'},
    'Cecil':{'phone':'3158','addr':'Baz Avenue 90'}
    }

#make some lable for printing:
labels = {'phone':'Phone Number: ',
          'addr':'Address: '}

name = input('Name: ')
request = input('phone number (p) or address (a)? ')

key=request
if request=='p': key='phone'
if request=='a': key='addr'


person=people.get(name,{})
label=labels.get(key,key)
result=person.get(key,'not available')

print ("{}'s {} is {}.".format(name,label,result))
