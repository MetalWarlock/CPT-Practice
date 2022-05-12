from re import sub
class Flying_object():
    def __init__(self,velocity, moving_time, stop_time):
        time = 2503
        self.range = 0
        count = 0
        change = 0
        while count < time:
            if change == 0:
                if count + moving_time < time:
                    self.range += velocity*moving_time
                else:
                    self.range += velocity*(time-count)
                count += moving_time
                change = 1
            elif change == 1:
                count += stop_time
                change = 0
            

a = []
with open('input.txt') as f:
    for line in f:
        line = sub(r'can fly | km/s for| (seconds, but then must rest for)| seconds.', '', line)
        a.append(line.split())

final = []
for e in a:
    obj = Flying_object(int(e[1]),int(e[2]),int(e[3]))
    final.append(obj.range)

with open('output1.txt','w') as f:
    f.write(str(max(final)))