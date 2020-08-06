pie = 22/7

a = [list(map(int, input().split())) for _ in range(int(input()))]
count = 0
for _ in a:
    if 2*_[0]*pie < _[1]*100:
        count+=1
print(count)