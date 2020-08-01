n = int(input())
a = list(map(int, input().split()))
 
min_val = float('inf')
pos_min = -1
sum_a = sum(a)
for i in range(n):
    temp = sum_a - a[i]
    if temp % 7 == 0:
        if min_val > a[i]:
            min_val = a[i]
            pos_min = i
print(pos_min)