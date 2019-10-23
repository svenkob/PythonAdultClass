n=int(input())
d=dict()
for i in range(n):
    c,*cities=input().split()
    d[c]=cities
#print(d)
n=int(input())
for i in range(n):
    c=input()
    for keys,values in d.items():
        if c in values:
            print(keys)


a=[]