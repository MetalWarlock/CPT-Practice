import re
i = "P"
with open("input.txt") as thing:
    M, N = 0, 0
    result = []
    for line in thing:
        trim_line = line[:-1]
        no_line = trim_line.replace("\\\\", i)
        no_quotes = no_line.replace("\\\"", i)
        no_hexcode_line = re.sub("\\\\x..", i, no_quotes)

        M += len(trim_line)
        N += (len(no_hexcode_line) - 2)
        result.append(trim_line)

with open('output1.txt', 'w') as f:
    print(str(M - N), file=f)