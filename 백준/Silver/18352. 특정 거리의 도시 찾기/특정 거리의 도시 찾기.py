from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

distance=[-1]*(n+1)
distance[x]=0

queue=deque([x])

while queue:
    now=queue.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now]+1
            queue.append(next)

result = []
for i in range(1,n+1):
    if distance[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    result.sort()
    for j in result:
        print(j)