x,y=list(map(int,input().split()))
a=int(str(x)[::-1])
b=int(str(y)[::-1])
if a<b:
    print(b)
else :
    print(a)