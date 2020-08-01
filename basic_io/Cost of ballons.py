n = int(input())
while n > 0:
    temp = [0, 0]
    min_total = 0
    green, purple = map(int, input().split())
    k = int(input())
    while k > 0:
        first, second = map(int, input().split())
        if first == 1: temp[0] += 1
        if second == 1: temp[1] += 1
        k -= 1
    print(min(green, purple) * max(temp) + max(green, purple) * min(temp))
    n -= 1
