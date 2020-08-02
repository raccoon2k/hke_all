n = int(input())

k = [input().split() for _ in range(n)]

for _ in k:
    if sorted(_[0]) == sorted(_[1]):
        print("YES")
    else: 
        print("NO")
