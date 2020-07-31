n = int(input())
k = int(input())
f_sum = 0
count = 0
# 

for _ in range(10**(n-1), 10**(n)):
    temp = [int(i) for i in str(_)]
    f_sum = sum(temp[:k])
    currrent_sum = 0
    for j in range(n):
        currrent_sum += temp[j]
        if j >= k - 1:
            if f_sum != currrent_sum:
                break
            currrent_sum -= temp[j-k+1]
        if j == n - 1:
            count += 1
print(count)
