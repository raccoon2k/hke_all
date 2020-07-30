n = int(input())
k = 0
tra_type = "none"
line1 = [11, 9, 7, 5, 3, 1]
line1_type = ["WS", "MS", "AS", "AS", "MS", "WS"]
line2 = [0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 9, 11]
line2_type = ["", "", "", "", "", "", "WS", "MS", "AS", "AS", "MS", "WS"]
while n > 0:
    k = int(input())
    t = k
    while k not in list(range(1, 13)):
        k -= 12
    if k in list(range(7)):
        t += line1[k-1]
        tra_type = line1_type[k-1]
    else:
        t -= line2[k-1]
        tra_type = line2_type[k-1]
    print(f'{t} {tra_type}')
    n -= 1
