k = int(input())

while k > 0:
    m, n = map(int, input().split())
    z = []
    max_len = [0 for _ in range(m)]
    for i in range(n + 1):
        c = input().split()
        z.append(c)
        for j in range(m):
            if len(c[j]) > max_len[j]:
                max_len[j] = len(c[j])

    for i in range(m):
        print(f"+{'-' * (max_len[i]+2)}", end="")
        if i == m - 1: print("+")

    for i in range(n + 1):
        for j in range(m):
            if z[i][j].isdigit():
                print(f"| {' ' * (max_len[j]- len(z[i][j]))}{z[i][j]} ",
                      end="")
            else:
                print(f"| {z[i][j]}{' ' * (max_len[j]+1 - len(z[i][j]))}",
                      end="")
        print("|")
        if i == 0:
            for _ in range(m):
                print(f"+{'-' * (max_len[_]+2)}", end="")
                if _ == m - 1: print("+")
        if i == n:
            for _ in range(m):
                print(f"+{'-' * (max_len[_]+2)}", end="")
                if _ == m - 1: print("+")
    k -= 1
