import json
import re

array = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        line = re.sub(r'(Sue) [0-9]+: ', '', line)
        propertys = re.findall(r'[A-Za-z]+', line)
        for element in propertys:
            line = re.sub(element, '\"' + element + '\"', line)
        line = '{' + line + '}'
        line = json.loads(line)
        array.append(line)

a = {"children": 3, "cats": 7, "samoyeds": 2 ,"pomeranians": 3 ,"akitas": 0\
       ,"vizslas": 0, "goldfish": 5,"trees": 3, "cars": 2, "perfumes": 1}

for i in range(len(array)):
    for j in a.keys():
        if j in array[i].keys():
            None
        else:
            array[i].update({j: None})

score_array = []
propertyes = a.keys()
for element in array:
    score = 0
    for j in element.items():
        if j in a.items():
            if j[0] == 'trees':
                if j[1] > a['trees']:
                    score += 1
            elif j[0] == 'cats':
                if j[1] > a['cats']:
                    score += 1
            elif j[0] == 'pomeranians':
                if j[1] < a['pomeranians']:
                    score += 1
            elif j[0] == 'goldfish':
                if j[1] < a['goldfish']:
                    score += 1
            else:
                score += 1
    score_array.append(score)

with open('output2.txt','w') as f:
    f.write(str(score_array.index(max(score_array))+1))