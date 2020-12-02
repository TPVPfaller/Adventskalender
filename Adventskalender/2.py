file = open("data2.txt", "r")
count = 0
for val in file.readlines():
    for i, x in enumerate(val.split(" ")):
        if i==0:
            low, up = x.split("-")
        elif i==1:
            c = x[0]
        elif i==2:
            s = x
    if (s[int(low)-1]==c and s[int(up)-1]!=c) or (s[int(up)-1] == c and s[int(low)-1]!=c):
        count += 1
print(count)