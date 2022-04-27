n=int(input())
if(n==1 or n==2):
    print (1)
for i in range(2,n):
    if(n%i==0):
        print (i)
        break
