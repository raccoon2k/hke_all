from sys import exit
a = input()
if len(a) != 10:
    print("Illegal ISBN")
    exit()
sum_k = 0
for i in range(1,11):
    sum_k+= int(a[i-1])*i
if sum_k % 11 != 0 :
    print("Illegal ISBN")
else : 
    print("Legal ISBN")