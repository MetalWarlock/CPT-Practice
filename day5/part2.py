with open('input.txt', encoding='utf-8') as f:
    str = f.readlines()

def is_good(str):

    if not any([str[i] == str[i+2] for i in range(len(str)-2)]):
        return False
    if any([(str.count(str[i:i+2])>=2) for i in range(len(str)-2)]):
        return True

    return False


i = 0
for line in str:
    if is_good(line):
        i += 1


with open("output2.txt", "w") as f:
    print(i, file = f)