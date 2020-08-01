const = int(input())
n = int(input())
while n > 0:
    a = ""
    w, h = map(int, input().split())
    if w < const or h < const: a = "UPLOAD ANOTHER"
    elif w == h: a = "ACCEPTED"
    else: a = "CROP IT"
    print(a)
    n -= 1
