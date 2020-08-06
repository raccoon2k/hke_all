n, q = map(int, input().split())

arr = [int(i) for i in input().split()]

for i in range(1, n):
    arr[i] = arr[i] + arr[i-1]

print(arr)

for _ in range(q):
    L, R = map(int, input().split())
    if L == 1:
        print(arr[R-1] // (R-L+1))
    else:
        print((arr[R-1] - arr[L-2]) // (R-L+1))
