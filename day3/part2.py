presents = []
santa = []
robot = []

f = open("input.txt")
a = list(f.read().strip())

for i in range(len(a)):
    if i%2 == 0:
        santa.append(a[i])
    if i%2 != 0:
        robot.append(a[i])

presents.append([0,0])
sx = 0
sy = 0
rx = 0
ry = 0

for i in range(len(santa)):
    if santa[i] == '>':
        sx += 1
    elif santa[i] == '<':
        sx -= 1
    elif santa[i] == '^':
        sy += 1
    elif santa[i] == 'v':
        sy -= 1
    if [sx,sy] not in presents:    
        presents.append([sx,sy])

for i in range(len(robot)):
    if robot[i] == '>':
        rx += 1
    elif robot[i] == '<':
        rx -= 1
    elif robot[i] == '^':
        ry += 1
    elif robot[i] == 'v':
        ry -= 1
    if [rx,ry] not in presents:    
        presents.append([rx,ry])

f = open("output2.txt","w")
f.write(str(len(presents)))
