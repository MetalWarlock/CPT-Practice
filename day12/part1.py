with open('input.txt') as f:
    string = f.readline()

for unit in string:
    if unit.isdigit() == False and unit != '-':
        string = string.replace(unit, '.')

a = []
b = []
a = string.split('.')
for unit in a:
    if unit != '':
        b.append(int(unit))

with open('output1.txt','w') as f:
    f.write(str(sum(b)))