from decimal import Decimal,ROUND_HALF_UP
a = [list(map(int, input().split())) for _ in range(int(input()))]

for i in a:
    temp_1 = i[1] - i[0]
    temp_2 = i[2] - i[1]
    mid = abs(max(temp_1, temp_2) - min(temp_1, temp_2)) / 2
    print(Decimal(mid).quantize(Decimal('1'),rounding=ROUND_HALF_UP))

