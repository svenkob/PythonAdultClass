import math
a = [int(s) for s in input().split()]
counter=0
for i in a:
    c=a.count(i)
    print(c)
    if c > 1:
        counter+=math.floor(c/2)
    for j in range(c):
        a.remove(i)

print("counter",counter)