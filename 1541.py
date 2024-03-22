import re

e = input()
numbers = re.split('[+-]', e)
numbers = [int(num) for num in numbers]
result = 0

formula = ['+']
for i in e:
    if i == '+' or i == '-':
        formula.append(i)

switch = True
for i, f in enumerate(formula):
    if f == '-' and switch == True:
        switch = not switch
    
    if switch:
        result += numbers[i]
    else:
        result -= numbers[i]


print(result)