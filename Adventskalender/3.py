file = open("data3.txt", "r")
m = []
for i, val in enumerate(file.readlines()):
    m.append(list())
    for x in val:
        if x != "\n":
            m[i].append(x)
n = len(m)-1
res=1
steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for h, v in steps:
    add = 0
    count = 0
    row = 0
    while row < n:
        i = 0
        i -= add
        while i < len(m[row])-h and row < n-v+1:
            i += h
            row += v
            if m[row][i] == "#":
                count += 1
            add = len(m[row])-i
    res *= count
print(res)