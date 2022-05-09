with open("input.txt") as thing:
    M, N = 0, 0
    result = []

    for ln in thing:
        trim_line = ln[:-1]
        escaped_quotes = trim_line.replace("\\", "\\\\")
        escaped_slashes = escaped_quotes.replace("\"", "\\\"")
        M += len(trim_line)
        N += (len(escaped_slashes) + 2)
        result.append(trim_line)


with open('output2.txt', 'w') as f:
    print(int(str(N - M))+1, file=f)