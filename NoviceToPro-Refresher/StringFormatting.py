#print a formatted price list with a given width

width=int(input('please enter width: '))
price_width = 10
item_width = (width - price_width)

header_format='%-*s%*s'
format = '%-*s%*.2f'

print (width*'=')
print(header_format %(item_width,'Item',price_width,'Price'))
print (width*'-')

print (format %(item_width,'apples',price_width,0.32))
print (format %(item_width,'bread',price_width,2.3))
print (format %(item_width,'Store Credit',price_width,-10))

print (width*'-')
