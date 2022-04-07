import hashlib

f = open('input.txt')
a = f.read()

i = 0

while True:
    b = a + str(i)
    result = hashlib.md5(b.encode())
    hexdigit = str(result.hexdigest())

    if hexdigit[0:5] == '00000':
        break
    else:
        i += 1

f = open("output1.txt","w")
f.write(str(i))
