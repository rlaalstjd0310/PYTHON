from collections import deque
import sys
input = sys.stdin.readline

x = input().strip()
dq = deque()
count = len(x)
half = int(count)//2
sum_left=0
sum_right=0
for i in range(half):
     sum_left+=int(x[i])


for l in range(count-half,count):
     sum_right+=int(x[l])

if sum_left == sum_right:
     print("LUCKY")
else:
     print("READY")


