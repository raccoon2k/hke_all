from sys import exit
tag = [_ for _ in input()]

a = int(tag[0]) + int(tag[1])
b = int(tag[3]) + int(tag[4])
c = int(tag[4]) + int(tag[5])
d = int(tag[7]) + int(tag[8])

if len(set(tag).intersection(set(["A", "E", "I", "O", "U", "Y"]))) != 0:
    print("invalid")
    exit()
if a % 2 != 0 or b % 2 != 0 or c % 2 != 0 or d % 2 != 0:
    print("invalid")
else:
    print("valid")
