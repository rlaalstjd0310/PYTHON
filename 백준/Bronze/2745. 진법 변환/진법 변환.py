import sys
input = sys.stdin.readline

x,y=input().split()
base = int(y)
number=x.upper()

result = int(number,base)
print(result)
