a,b,c=map(int,input().split())
if a==b and b==c and c==a:
    print(10000+a*1000)
if {a==b and b!=c and c!=a} or {b==c and c!=a and a!=b} or {a==c and a!=b and b!=c}:
    if a==b and b!=c and c!=a:
        print(1000+a*100)
    elif b==c and a!=b and a!=c:
        print(1000+b*100)
    elif c==a and b!=a and b!=c:
        print(1000+c*100)
if a!=b and b!=c and c!=a:
    if a>b and a>c:
        print(a*100)
    elif b>a and b>c:
        print(b*100)
    elif c>a and c>b:
        print(c*100)