def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        if(prime(i)):
            print(i,end=' ')
            c+=1
if c==0:
    print('-1')