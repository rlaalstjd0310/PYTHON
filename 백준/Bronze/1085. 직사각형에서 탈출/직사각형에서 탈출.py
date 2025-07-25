import sys
input = sys.stdin.readline
a,b,c,d=map(int,input().split())
sx=0
sy=0
if a<c-a:
    sx=a
else:
    sx=c-a

if b<d-b:
    sy=b
else:
    sy=d-b

if sx<sy:
    print(sx)
else:
    print(sy)

