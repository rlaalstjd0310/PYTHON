from collections import deque
import sys
input = sys.stdin.readline

x = int(input())
dq = deque()

for i in range(1,x+1):
     dq.append(i)

for l in range(x-1):
     dq.popleft()
     if not dq:
          break
     k =dq.popleft()
     dq.append(k)

print(dq[0])
