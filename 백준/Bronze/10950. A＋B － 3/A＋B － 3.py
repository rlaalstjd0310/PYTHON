i=int(input())
r = []
n=0
for a in range(i):
    x,y = map(int,input().split())
    r.append(x+y)
for z in range(i):
    print(r[n])
    n+=1