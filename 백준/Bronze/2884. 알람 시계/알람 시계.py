a,b=input().split()
x=int(a)
y=int(b)
if x>0:
    if y<45:
        print(x-1,y+15)
    elif y>=45:
        print(x,y-45)
elif x==0:
    if y<45:
        print(x+23,y+15)
    elif y>=45:
        print(x,y-45)