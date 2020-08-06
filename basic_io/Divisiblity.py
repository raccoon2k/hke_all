n = int(input())

k = []
num = 0
z = [i for i in input().split()]

num = int(z[n-1][-1:])

print("Yes") if num % 10 == 0 else print("No")
