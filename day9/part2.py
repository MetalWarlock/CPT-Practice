import re, itertools

def calc(f):
    places = set()
    distance = {}

    for line in f:
        start, end = line.split(" ")[0], line.split(" ")[2]

        places.add(start)
        places.add(end)

        distance_between = int(re.findall("\d+", line)[0])
        distance[(start, end)] = distance_between
        distance[(end, start)] = distance_between

    return places, distance


with open("input.txt") as f1:
    (places, distance) = calc(f1)

    path_lengths = {}

    for path in itertools.permutations(places):
        segments = [(path[i], path[i + 1]) for i in range(0, len(places) - 1)]
        lengths = [distance[segment] for segment in segments]

        path_lengths[path] = sum(lengths)

with open('output2.txt', 'w') as f2:
    print(str(max(path_lengths.values())), file=f2)