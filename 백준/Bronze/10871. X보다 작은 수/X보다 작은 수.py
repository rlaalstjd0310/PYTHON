a,b=map(int,input().split())
c=list(map(int,input().split()))
l=[]
e=0

while e<a:
    if c[e]<b:
        l.append(c[e])
    e+=1
print(*l)
