for i in range(int(input())):
    n = input()
    k = 0
    for j in n:
        j = int(j)
        if j in [2, 3, 5]:
            k += 5
        elif j in [0, 6, 9]:
            k += 6
        elif j == 1:
            k += 2
        elif j == 7:
            k += 3
        elif j == 4:
            k += 4
        else:
            k += 7
    if k % 2 == 0:
        for i in range(k//2):
            print("1", end="")
        print()
    else:
        temp = k // 2
        print("7",end="")
        for i in range(temp-1):
            print('1', end="")
        print()
