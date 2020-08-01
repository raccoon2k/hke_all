from sys import exit
n = int(input())

a = [_ for _ in input()]

for i in range(n):
    if a[i] == "H":
        if i == n - 1: break
        if a[i + 1] == "H":
            print("NO")
            exit()
        elif a[i + 1] == ".":
            a[i + 1] = "B"
    if a[i] == ".": a[i] = "B"
k = ""
for _ in a:
    k += _
print(f"YES\n{k}")
