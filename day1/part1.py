f = open("input.txt")
a = list(f.read())
f = open("output1.txt","w")
f.write(str(a.count("(") - a.count(')')))
