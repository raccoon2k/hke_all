n = int(input())
l_A = [0, 'A']
l_B = [7, 'B']
lis = [int(input()) for _ in range(n)]
for k in lis:
    temp_1 = abs(l_A[0] - k)
    temp_2 = abs(l_B[0] - k)
    if temp_1 < temp_2:
        print("A")
        l_A[0] = k
    elif temp_1 > temp_2:
        print("B")
        l_B[0] = k
    else:
        temp_3 = min(l_A, l_B)
        print(temp_3[1])
        temp_3[0] = k