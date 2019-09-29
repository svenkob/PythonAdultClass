n=int(input("Please enter a number of rows: "))
m=int(input("Please enter a number of columns: "))
k=int(input("Please enter a number of pieces: "))
total=n*m
if (total < k):
    print("NO")
elif k%n==0 or k%m==0:
    print("YES")
else:
    print("NO")