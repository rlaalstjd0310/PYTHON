t= int(input())
n=list(map(int,input().split()))
n.sort()
print(n[0],n[t-1])