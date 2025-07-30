import sys
input = sys.stdin.readline
a,b=map(int,input().split())
n=list(map(int,input().split()))
m=0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if n[i] + n[j] + n[k] > b:
                continue    
            else:
                m = max(m,n[i]+n[j]+n[k])
print(m)