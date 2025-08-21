from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))
op=list(map(int,input().split()))

mx=-sys.maxsize
mn=sys.maxsize

def bfs():
    global mx,mn
    queue = deque([(numbers[0],1,op[0],op[1],op[2],op[3])])

    while queue:
        current , k, plus, minus,mul,div = queue.popleft()

        if k == n:
            mx = max(mx,current)
            mn = min(mn,current)
            continue

        if plus>0:
            new = current + numbers[k]
            queue.append((new,k+1,plus-1,minus,mul,div))

        if minus>0:
            new = current - numbers[k]
            queue.append((new,k+1,plus,minus-1,mul,div))

        if mul>0:
            new = current * numbers[k]
            queue.append((new,k+1,plus,minus,mul-1,div))

        if div>0:
            if current<0:
                new = -(abs(current)//numbers[k])
            else:
                new = current // numbers[k]
            queue.append((new,k+1,plus,minus,mul,div-1))
bfs()

print(mx)
print(mn)