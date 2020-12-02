file = open("data1.txt", "r")
data = []
for val in file.read().split():
    data.append(int(val))
data.sort()
n = len(data)
for i, val in enumerate(data):
    pos1 = i+1
    pos2 = pos1+1
    while pos1<n:
        pos2 = pos1+1
        if val + data[pos1]>2020:
            break
        while pos2<n:
            if val + data[pos1] + data[pos2] == 2020:
                print(val*data[pos1]*data[pos2])
            elif val + data[pos1] + data[pos2] > 2020:
                break
            else:
                pos2+=1
        pos1+=1
