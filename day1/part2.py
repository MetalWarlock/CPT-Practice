floor = 0
f = open("input.txt")
a = list(f.read())

for i in range(len(a)):
    if floor >= 0:
        if a[i] == '(':
            floor += 1
        elif a[i] == ')':
            floor -= 1
    else:
        floor = i
        break
f = open("output2.txt","w")
f.write(str(floor))
