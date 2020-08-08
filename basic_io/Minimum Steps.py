from math import ceil


def find_min(a, b, c):
    if a >= b:
        return ceil((a-b) / 2)
    if b % c == 0:
        return 1 + find_min(a, b // c, c)
    else:
        x = (b//c + 1) *c
        return (ceil((x-b) / 2) + find_min(a, x, c))


for i in range(int(input())):
    k, m, n = map(int, input().split())
    print(find_min(k, m, n))
