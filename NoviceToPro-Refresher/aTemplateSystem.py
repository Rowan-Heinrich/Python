#aTemplateSystem.py
import fileinput, re

#matches fields enclosed in square brackets:
field_pat = re.compile(r'\[(.+?)\]')

scope = {}

def replacement(match):
    code = match.group(1)
    try:
        #If the field can be evaluated, return it:
        return str(eval(code,scope))
    except SyntaxError:
        #Otherwise execute the assignment in the same scope...
        exec(code) in scope
        #... and return an empty string; 
        return ''

#get all the text as a single string:
lines =[]
for line in fileinput.input('C:\\Users\\Rowan\\Documents\\GitHub\\Python\\NoviceToPro-Refresher\\SampleTextDocs\\simpleTemplateReplace.txt'):
    lines.append(line)
text = ''.join(lines)

print(field_pat.sub(replacement, text))
