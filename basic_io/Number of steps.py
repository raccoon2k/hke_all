from sys import exit
n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]

key = min(a)
step = 0
i = 0
while i < n:
    j = a[i]
    while j > key:
        j = j - b[i]
        step = step + 1
    if j == key:
        i += 1
        continue
    if j < key:
        if j < 1:
            print(-1)
            exit(0)
        else:
            key = j
            i = 0
            step = 0
            continue
print(step)
