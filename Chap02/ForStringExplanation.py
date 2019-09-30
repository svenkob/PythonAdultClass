s = 'abcdefg'

#print(s[1])
#print(s[-1])
#print(s[1:3])
#print(s[1:-1])
#print(s[:3])
#print(s[2:])
#print(s[:-1])
#print(s[::2])
#print(s[1::2])
print(s[2:1:-1])

for i in s:
    print(i)
for idx in range(0,len(s),2):
    print(s[idx])
s="abc"
s[0]='g'
ouput="g" + s[1:]