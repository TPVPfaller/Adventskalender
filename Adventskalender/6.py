from collections import defaultdict


count = 0

with open("data6.txt") as f:
    x = ""
    amount = 0
    for line in f.readlines():
        if line == "\n":
            m = [0]*26
            for c in x:
                m[ord(c) - 97] += 1
            for k in range(26):
                if m[k] >= amount:
                    count += 1
            x = ""
            amount = 0
        else:
            amount += 1
            for i in line:
                if i != "\n":
                    x += i
    m = [0] * 26
    for c in x:
        m[ord(c) - 97] += 1
    for k in range(26):
        if m[k] >= amount:
            count += 1
print(count)