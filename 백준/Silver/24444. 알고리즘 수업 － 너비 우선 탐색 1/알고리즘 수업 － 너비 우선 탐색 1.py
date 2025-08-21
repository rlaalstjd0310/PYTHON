from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
count=1
def bfs(graph,node,visited):
    global count
    queue = deque([node])

    visited[node] = count
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                count+=1
                visited[i] = count

n,m,r=map(int,input().split())
graph= [[] for _ in range(n+1)]

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [0] * (n+1)
for i in graph:
    i.sort()

bfs(graph,r,visited)

for j in range(1,n+1):
    print(visited[j])