presents = []

f = open("input.txt")
a = list(f.read().strip())

presents.append([0,0])
x = 0
y = 0

for i in range(len(a)):
    if a[i] == '>':
        x += 1
    elif a[i] == '<':
        x -= 1
    elif a[i] == '^':
        y += 1
    elif a[i] == 'v':
        y -= 1
    if [x,y] not in presents:    
        presents.append([x,y])

f = open("output1.txt","w")
f.write(str(len(presents)))
