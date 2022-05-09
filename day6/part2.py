matrix = [[0 for x in range(1000)] for y in range(1000)]

with open('input.txt') as f:
    things = f.readlines()

for thing in things:
    if 'on' in thing or 'off' in thing:
        a = thing.split()
        instruction = a[1]
        begin = a[2]
        end = a[4]
    else:
        a = thing.split()
        instruction = a[0]
        begin = a[1]
        end = a[3]

    x_begin, y_begin = begin.split(",")
    x_end, y_end = end.split(",")

    for x in range(int(x_begin), int(x_end) + 1):
        for y in range(int(y_begin), int(y_end) + 1):

            if instruction == "toggle":
                matrix[x][y] += 2

            if instruction == "on":
                matrix[x][y] += 1

            if instruction == "off" and matrix[x][y] != 0:
                matrix[x][y] -= 1


count = 0
for i in range(1000):
    for j in range(1000):
        count += matrix[i][j]

with open('output2.txt', 'w') as f:
    print(count, file=f)