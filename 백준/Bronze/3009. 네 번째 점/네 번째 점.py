import sys
input = sys.stdin.readline
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())

if a == c:
    g = e
elif a==e:
    g = c
elif c==e:
    g = a

if b==d:
    h = f
elif b == f:
    h = d
elif d==f:
    h = b

print(g, h)