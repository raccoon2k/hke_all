# Write your code here
N = int(input())

ns = [int(n) for n in input().split()]

k = 2
start = 1
while start + k <= N:
    start += k
    k += 1
k-=1
s = sum(ns[:start])
ms = s

for i in range(1, N):
    s -= ns[i - 1]
    if start < N:
        s += ns[start]
        start += 1
    else:
        k -= 1
        s -= sum(ns[N - k:N])
        start -= k
    if s > ms:
        ms = s
print(ms)
