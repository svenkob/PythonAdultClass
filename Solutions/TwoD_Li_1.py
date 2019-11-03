n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][i] = 1
for i in range(n):
    for j in range(0, i):
        a[i][j]=2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()