import collections as colect

n = int(input())

while n > 0:
    str1 = [char for char in input()]
    str2 = [_ for _ in input()]
    res = 0
    temp1 = list(set(str1))
    temp2 = list(set(str2))
    a = colect.Counter(str1)
    b = colect.Counter(str2)
    max_ab = 0
    min_ab = 0
    set_max = 0
    set_min = 0
    lena = len(a)
    lenb = len(b)
    if lena > lenb:
        set_max = temp1
        set_min = temp2
        max_ab = a
        min_ab = b
    else:
        set_max = temp2
        set_min = temp1
        max_ab = b
        min_ab = a
    for i in set_min:
        res += abs(a[i] - b[i])
    for i in set_max:
        if i not in set_min:
            res += max_ab[i]
    print(res)
    n -= 1
