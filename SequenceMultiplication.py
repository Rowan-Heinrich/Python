#Prints a sentence in a centered 'Box' of correct width
#note the interger division operator(//) only works in python 2.
#use plain division in Python 3.

sentence = input("Sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = int((screen_width - box_width)/2)

print()
print(' '*left_margin+'+'+'-'*(box_width-2)+'+')
print(' '*left_margin+'|  '+' '*(text_width) +'  |')
print(' '*left_margin+'|  '+sentence+'  |')
print(' '*left_margin+'|  '+' '*text_width +'  |')
print(' '*left_margin+'+'+'-'*(box_width-2)+'+')
