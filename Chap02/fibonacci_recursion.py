def fibonacci_recur(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return(fibonacci_recur(n-1)+fibonacci_recur(n-2))

print(fibonacci_recur(6))