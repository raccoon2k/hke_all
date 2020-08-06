n = int(input())

a = input().split()

check = int(a[0][0])
for i in range(1, n//2):
    if i % 2 != 0:
        check -= int(a[i][0])
    else:
        check += int(a[i][0])
for i in range(n//2, n):
    if i % 2 != 0:
        check -= int(a[i][-1:])
    else:
        check += int(a[i][-1:])

print("OUI") if check % 11 == 0 else print("NON")
