x,y=map(int,input().split())
m=list(range(1,x+1))
for i in range(1,1+y):
    a,b=map(int,input().split())
    m[a-1],m[b-1] = m[b-1],m[a-1]
print(*m)