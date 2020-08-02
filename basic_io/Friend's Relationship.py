a = [int(input()) for i in range(int(input()))]

for i in a:
    start = 1
    tag = i - 1
    while i > 0:
        d = ['*' for _ in range(start)]
        b = ["#" for _ in range(tag)]
        k = ""
        k = k.join(d + b)
        print(f'{k}{k[::-1]}')
        start += 1
        tag -= 1
        i -= 1
