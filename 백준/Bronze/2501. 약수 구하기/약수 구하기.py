import sys
input = sys.stdin.readline

x,y=map(int,input().split())
arr=[]

for i in range(1,x+1):
    if x%i == 0:
        arr.append(i)

if y>len(arr):
    print(0)
else:
    print(arr[y-1])