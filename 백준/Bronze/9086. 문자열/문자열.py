t=int(input())

for _ in range(t):
    k=input()
    if len(k) == 1:
        print(k*2)
    else:
        print(k[0]+k[-1])