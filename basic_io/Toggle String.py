temp = [_ for _ in input()]

for _ in range(len(temp)):
    if temp[_].isupper(): temp[_] = temp[_].lower()
    else: temp[_] = temp[_].upper()
a = ""
for _ in temp:
    a += _
print(a)