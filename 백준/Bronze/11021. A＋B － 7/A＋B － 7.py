t=int(input())
r=[]
n=1
k=0
for x in range(1,t+1):
    a,b=map(int,input().split())
    r.append(a+b)
for n in range(1,t+1):
    print(f"Case #{n}: {r[k]}")
    n+=1
    k+=1