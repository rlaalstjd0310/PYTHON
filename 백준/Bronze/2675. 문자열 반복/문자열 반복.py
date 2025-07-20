t=int(input())  #case개수

for i in range(t):
    x,y=input().split()
    x=int(x)
    for _ in y:
        print(_*x,end="")
    print()
