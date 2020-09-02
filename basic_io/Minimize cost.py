n, k = map(int, input().split(" "))

arr = [int(_) for _ in input().split(" ")]

j = 0

for i in range(n):
    if arr[i] < 0:
        continue
    while j not in range(i-k, i+k+1):
        j += 1
    while arr[i] > 0 and j <= min(i+k, n-1):
        if arr[j] < 0:
            temp = min(abs(arr[j]), arr[i])
            arr[i] -= temp
            arr[j] += temp
        else:
            j+=1
print(sum(abs(_) for _ in arr))
