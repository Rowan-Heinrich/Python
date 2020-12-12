def fibs(num):
    'Calculates the fibonacci numbers for a given range'
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

print(help(fibs))
a=fibs(int(input('How many number? ')))
print(a)
