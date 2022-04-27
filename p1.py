l=list()
m=list()
n=int(input("enter number:"))
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()    
for j in range(n-1):
    b=l[j]-l[j+1]
    m.append(abs(b))
g=0    
for k in range(len(m)):
    g=g+m[k]
print(g)    
