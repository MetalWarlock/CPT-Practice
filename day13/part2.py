import itertools as it

a = []
b = []

with open('input.txt') as f:
    for line in f:
        line = line.replace('happiness units by sitting next to', '')
        line = line.replace('would', '')
        line = line.replace('.', '')
        line = line.strip()
        if 'gain' in line:
            line = line.replace('gain ', '')
        else:
            line = line.replace('lose ', '-')

        a_1 = line.split()
        a_1[1] = int(a_1[1])
        a.append(a_1)
        if a_1[0] not in b:
            b.append(a_1[0])
for d in b:
    a.append(['Me', 0, d])
b.append('Me')

names = list(it.permutations(b))

c = []
for e in names:
    score = 0
    for i in range(len(e)):
        if i == 0:
            for e_1 in a:
                if (e[i] == e_1[0]) and (e[i+1] == e_1[2]):
                    score += e_1[1]
            for e_1 in a:
                if (e[i] == e_1[0]) and (e[-1] == e_1[2]):
                    score += e_1[1]
        elif i == len(e) - 1:
            for e_1 in a:
                if (e[i] == e_1[0]) and (e[0] == e_1[2]):
                    score += e_1[1]
            for e_1 in a:
                if (e[i] == e_1[0]) and (e[i-1] == e_1[2]):
                    score += e_1[1]
            c.append(score)
        else:
            for e_1 in a:
                if (e[i] == e_1[0]) and (e[i+1] == e_1[2]):
                    score += e_1[1]
            for e_1 in a:
                if (e[i] == e_1[0]) and (e[i-1] == e_1[2]):
                    score += e_1[1]
                    
with open('output2.txt','w') as f:
    f.write(str(max(c)))