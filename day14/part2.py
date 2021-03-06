from re import sub

class Flying_object():
    def __init__(self, velocity, moving_time, stop_time, time):
        self.time = time
        self.distance = 0
        self.timer = 0
        self.moving_time = moving_time
        self.stop_time = stop_time
        self.velocity = velocity
        self.local_timer = moving_time
        self.End = False
        self.switcher = 0
        
    def counter(self):
        self.timer += 1
        if self.local_timer <= 0:
            if self.switcher == 1:
                self.switcher = 0
                self.local_timer = self.moving_time
            elif self.switcher == 0:
                self.switcher = 1
                self.local_timer = self.stop_time
        self.local_timer -= 1
        if self.switcher == 0:
            self.distance += self.velocity
        elif self.switcher == 1:
            None
        if self.timer == self.time:
            self.End = True

array = []
with open('input.txt','r') as f:
    for line in f:
        line = sub(r'can fly | km/s for| (seconds, but then must rest for)| seconds.', '', line)
        array.append(line.split())

final_array = []
names_array = []
class_array = []
for element in array:
    names_array.append(element[0])
    element[0] = Flying_object(int(element[1]),int(element[2]),int(element[3]), 2503)
    class_array.append(element[0])

score = [0 for i in range(len(names_array))]
while True:
    try:
        distance_array = []
        for element in class_array:
            if element.End == True:
                raise ZeroDivisionError
            element.counter()
            distance_array.append(element.distance)
        for i in range(len(distance_array)):
            if distance_array[i] == max(distance_array):
                WGS = i
                score[i] += 1
    except ZeroDivisionError:
        break

for index in range(len(score)):
    if score[index] == max(score):
        Index = index
        break
winner_name = names_array[Index]
    
with open('output2.txt','w') as f:
    f.write(str(max(score)))