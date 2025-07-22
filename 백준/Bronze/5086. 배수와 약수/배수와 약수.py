import sys
input = sys.stdin.readline

while True:
    x,y=map(int,input().split())
    if x>y:
        if x%y == 0:
            print("multiple")
        elif x%y !=0:
            print("neither")

    elif x<y:
        if y%x == 0:
            print("factor")
        elif y%x !=0:
            print("neither")

    elif x==y:
        exit()