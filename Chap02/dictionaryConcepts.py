sd={"pranav":13, input():"secret"}
sd["Pranav"]=[13,"grade10"]
sd["vishal"]=15
sd["lavan"]=14

print(sd)
s="vishal"
print("the age of", s, "is", sd[s])
print(sd.items())
for key,value in sd.items():
    print("The value for key",key,"is",value)
print(sd.keys())


print(sd.get("hello"))

a= ["satish", "satish", "pranav"]
countw={}
for i in a:
    countw[i]=0
print(countw)
for i in a:
        countw[i]=countw[i]+1
print(countw)
