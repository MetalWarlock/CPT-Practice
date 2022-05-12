def changer(json_file):
    if type(json_file) == list and json_file != []:
        return sum(changer(unit) for unit in json_file)
    elif type(json_file) == dict and 'red' in json_file.values():
        return 0
    elif type(json_file) == str:
        return 0
    elif type(json_file) == int:
        return json_file
    elif type(json_file) == dict:
        return changer(list(json_file.values()))

import json
with open('input.txt') as f:
    data = f.readline()

score = changer(json.loads(data))

with open('output2.txt', 'w') as f:
    f.write(str(score))
