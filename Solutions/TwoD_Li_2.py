#brute force method
n,m=[int(i) for i in input().split()]
row_sym="*"
a=[['.']*m for i in range(n)]
for i in range(n):
    if row_sym=='*':
        row_sym='.'
    else:
        row_sym='*'
    col_sym=row_sym
    for j in range(m):
        a[i][j]=col_sym
        if col_sym=='*':
            col_sym='.'
        else:
            col_sym='*'
x=[' '.join(a[i]) for i in range(n)]
[print(x[i]) for i in range(n)]

#Good method.
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))