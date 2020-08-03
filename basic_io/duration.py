
a = [[int(i) for i in input().split()] for _ in range(int(input()))]

for i in a:
    h = i[2] - i[0]
    m = i[3] - i[1]
    if m < 0:
        h -= 1
        m = 60 - abs(m)
    print(f"{h} {m}")