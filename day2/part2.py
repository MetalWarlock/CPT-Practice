Pf = 0
f = open("input.txt")
a = f.readlines()
for i in range(len(a)):
    b = list(map(int, a[i].split("x")))
    p1, p2, p3 = 2*b[0] + 2*b[1], 2*b[1] + 2*b[2], 2*b[0] + 2*b[2]
    P = min(p1,p2,p3)
    Pe = b[0]*b[1]*b[2]
    Pf += (Pe + P)

f = open("output2.txt","w")
f.write(str(Pf))
