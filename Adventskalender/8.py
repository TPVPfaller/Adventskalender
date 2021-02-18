import re

cmds = list()
values = list()
with open("data8.txt") as f:
    for line in f.readlines():
        c, v = line.split(" ")
        cmds.append(c)
        values.append(int(re.sub(r"\+", "", v[:-1])))


def check(pos):
    if cmds[pos] == "nop":
        cmds[pos] = "jmp"
    else:
        cmds[pos] = "nop"
    visited = [0] * len(cmds)
    res = 0
    c = 1
    index = 0
    while c:
        if index >= len(cmds):
            return res
        if visited[index]:
            if cmds[pos] == "nop":
                cmds[pos] = "jmp"
            else:
                cmds[pos] = "nop"
            return 0
        visited[index] = 1
        if cmds[index] == "nop":
            v.append(index)
            index += 1
        elif cmds[index] == "acc":
            res += values[index]
            index += 1
        elif cmds[index] == "jmp":
            v.append(index)
            index += values[index]
    return 0

visited = [0]*len(cmds)
v = list()
res = 0
c = 1
index = 0
while c:
    if visited[index]:
        break
    visited[index] = 1
    if cmds[index] == "nop":
        v.append(index)
        index += 1
    elif cmds[index] == "acc":
        index += 1
    elif cmds[index] == "jmp":
        v.append(index)
        index += values[index]

for x in reversed(v):
    res = check(x)
    if res != 0:
        print(res)
        break