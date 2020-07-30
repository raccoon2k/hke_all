n = input()
a = list(map(int, input().split(' ')))
res = 1
for i in a:
    res = (res*i) % ((10**9)+7)
print(res)
