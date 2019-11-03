numbers = int(input())
answer = 0
while numbers != 0:
    if numbers%2==0:
        answer+=1
    numbers= int(input())
print(answer)