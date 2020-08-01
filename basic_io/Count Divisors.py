l, r, k = map(int, input().split())
cout = 0
for _ in range(l, r + 1):
    if (_ % k == 0): cout += 1
print(cout)