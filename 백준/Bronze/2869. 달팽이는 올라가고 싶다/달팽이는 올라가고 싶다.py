import sys
import math
input = sys.stdin.readline
x,y,z=map(int,input().split())

rd = x - y
bd = z - x
if bd <=0:
    td = 0

else:
    td = math.ceil(bd/rd)

k = td+1

print(k)