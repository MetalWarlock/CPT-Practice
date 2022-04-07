Sf = 0
f = open("input.txt")
a = f.readlines()
for i in range(len(a)):
    b = list(map(int, a[i].split("x")))
    s1, s2, s3 = b[0]*b[1], b[1]*b[2], b[0]*b[2]
    Se = min(s1,s2,s3)
    S = (s1 * 2 + s2 * 2 + s3 * 2) + Se
    Sf += S

f = open("output1.txt","w")
f.write(str(Sf))
