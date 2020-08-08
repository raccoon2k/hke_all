def find_r(a,k):
    r = ord(a)
    s = ord('A')
    e = ord('Z')
    if a.islower():
        s = ord('a')
        e = ord('z')
    for _ in range(k):
        r += 1
        if r == e + 1:
            r = s
    return r



p = [i for i in input()]
k = int(input())
for i in range(len(p)):
    if p[i].isdigit():
        num = int(p[i]) + k
        if num > 9:
            p[i] = str((num % 10))
        else:
            p[i] = str(num)
    elif p[i].isalpha() and p[i].islower():
        num = ord(p[i]) + k
        if num > ord('z'):
            p[i] = chr(find_r(p[i],k))
        else:
            p[i] = chr(num)
    elif p[i].isalpha() and p[i].isupper():
        num = ord(p[i]) + k
        if num > ord('Z'):
            p[i] = chr(find_r(p[i],k))
        else:
            p[i] = chr(num)
c = ""
print(c.join(p))
