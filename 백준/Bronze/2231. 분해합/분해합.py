import sys
input = sys.stdin.readline
n=int(input())
z=[]
for i in range(1,n+1):
    s=0
    si=str(i)
    for k in si:
        s+=int(k)
    if i+s ==n:
        print(i)
        sys.exit()
print(0)