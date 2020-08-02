from collections import Counter

n = int(input())

a = [input().split() for _ in range(n)]

for _ in a:
    c1 = Counter(_[0])
    c2 = Counter(_[1])
    print("YES") if c1 == c2 else print("NO")
