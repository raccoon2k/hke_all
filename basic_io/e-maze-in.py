a = input()
b = [0, 0]
for _ in a:
    if _ == "R":
        b[0] += 1
    elif _ == "L":
        b[0] -= 1
    elif _ == "D":
        b[1] -= 1
    else:
        b[1] += 1
print(f'{b[0]} {b[1]}')