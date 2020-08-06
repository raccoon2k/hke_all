from sys import exit
n = int(input())

temp = 0
i = 1
while temp < n:
    temp = i + i + i
    if temp == n:
        print("YES")
        exit()
    tem = 0
    i = i + 1
print("NO")
