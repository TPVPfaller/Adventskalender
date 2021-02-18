with open("data5.txt") as f:
    original_seats = f.readlines()
seats = []
for s in original_seats:
    s = s.replace("\n", "")
    row = int(s[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(s[-3:].replace('L', '0').replace('R', '1'), 2)

    seat_id = row * 8 + col
    if row != 0 and row != 127:
        seats.append(seat_id)
print(seats)
seats.sort()
print(seats)
for i in range(1, len(seats)-1):
    if seats[i] == seats[i-1]+1 == seats[i+1]-1:
        pass
    else:
        print(seats[i])

