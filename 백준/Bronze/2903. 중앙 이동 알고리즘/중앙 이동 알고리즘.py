import sys
input = sys.stdin.readline

x=int(input())
n=2
for i in range(x):
    n = (2*n-1)
    point = n**2
print(point)