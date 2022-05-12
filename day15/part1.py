from itertools import dropwhile, combinations
import numpy as np

with open('input.txt') as f:
    ingredients = []
    new = []
    for line in f:
        line = line.replace(':', ' ')
        line = line.replace(',',' ')
        array = line.split()
        ingredients.append(array[0])
        array_1 = array.copy()
        for element in array:
            if element.isalpha() == True:
                array_1.remove(element)
        for i in range(len(array_1)):
            array_1[i] = int(array_1[i])
        new.append(array_1)
        array_1 = []
array = new

combined = []
for i in range(101):
    for j in range(101):
        for k in range(101):
            h = 100 - i - j - k
            if h >= 0:
                combined.append([h,i,j,k])

new_array = []
for i in range(len(array)):
    for j in range(len(array)):
        array_1.append(array[j][i])
    new_array.append(array_1)
    array_1 = []
array = new_array
new_array = []
for i in range(len(array)):
    new_array.append(np.array(array[i]))
for i in range(len(new_array)):
    new_array[i] = new_array[i].transpose()
array = new_array
new_array = []

some_list = []
produce = 1
check = []
ch = []
for element in combined:
    for ar in array:
        summ = ar.dot(np.array(element))
        if  summ < 0:
            summ = 0
        check.append(summ)
        produce *= summ
    ch.append(check)
    check = []
    some_list.append(produce)
    produce = 1

with open('output1.txt', 'w') as f:
    f.write(str(max(some_list)))