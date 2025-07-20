x,y=map(int,input().split())
m=[0]*x
for q in range(y):
    i,j,k = map(int,input().split())
    for a in range(i-1,j):
        m[a]=k
print(*m)