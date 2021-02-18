file = open("data4.txt", "r")
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
s = ""
count = 0
for val in file.readlines():
    if val in ['\n', '\r\n']:
        if all(field in s for field in fields):
            count += 1
        s = ""
    else:
        s += val
print(count)