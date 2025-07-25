import sys
input = sys.stdin.readline
while True:
    a,b,c=map(int,input().split())

    if a==0 and b==0 and c==0:
            break
    mx = max(a,b,c)

    if mx < (a+b+c-mx):
        if a==b and b==c and c==a:
            print("Equilateral")
        elif a==b or b==c or c==a:
            print("Isosceles")
        elif a!=b and b!=c and c!=a:
            print("Scalene")
            
    else:
        print("Invalid")