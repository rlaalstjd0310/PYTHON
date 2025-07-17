from collections import deque
import sys
input = sys.stdin.readline

x = int(input())
dq = deque()

for i in range(x):
    y = list(map(int, input().split()))
    k = y[0]

    if k == 1:
        dq.appendleft(y[1])
    elif k == 2:
        dq.append(y[1])
    elif k == 3:
        if not dq:
            print("-1")
        else:
            print(dq.popleft())
    elif k == 4:
        if not dq:
            print("-1")
        else:
            print(dq.pop())
    elif k == 5:
        print(len(dq))
    elif k == 6:
        print("0" if dq else "1")
    elif k == 7:
        if not dq:
            print("-1")
        else:
            print(dq[0])
    elif k == 8:
        if not dq:
            print("-1")
        else:
            print(dq[-1])
