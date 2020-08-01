from sys import exit
n = int(input())
i = 0
while n >= 0:
    i += 1
    n -= i
    if n <= 0:
        print("Patlu")
        exit()
    n -= (i * 2)
    if n <= 0:
        print("Motu")
        exit()
