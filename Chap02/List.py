a= [1,2,3]
b=[]
b= [0] *4

twoDimentional=[[1,2],[3,4],[7,8]]

print(twoDimentional)
anotherTwoDList=[]

anotherTwoDList.append([1,2])
print(anotherTwoDList)
s= input()
print(s)
anotherL=[int(i) for i in s.split() if i!='n']
print(anotherL)


b=[[1]*10]*5
print(b)
print(b)
b[0][1]=2
print(b)

b=[]
for i in range(5):
    b.append([0 for j in range(5)])

b[0][1]=2
print(b)

for i in b:
    print(i)
    for j in i:
        print(j)

for i in range(5):
    print(b[i])
    for j in range(5):
        print(b[i][j])


