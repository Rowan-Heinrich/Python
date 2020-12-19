#LineNumbers.py
import fileinput

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    #print(line,' #',num)

