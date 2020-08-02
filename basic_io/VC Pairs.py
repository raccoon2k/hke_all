
const = ['u','e','o','a','i']
count = 0
for _ in range(int(input())):
    n = int(input())
    test = input()
    for i in range(n-1):
        if test[i] not in const:
            if test[i+1]  in const: 
                count+=1
                i+=2
    print(count)
    count = 0