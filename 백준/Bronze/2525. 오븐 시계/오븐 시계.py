a, b = input().split()
c=input()
x=int(a)
y=int(b)
z=int(c)
k=(y+z)//60
t=(y+z)%60
if y+z<60:
    print(x,y+z)
elif y+z==60:
    if x+1==24:
        print(0,0)
    else:    
        print(x+1,0)
elif y+z>60:
        if x+k==24:
             print(0,t)
        elif x+k>24:
            print((x+k)%24,t)
        else:
            print(x+k,t)