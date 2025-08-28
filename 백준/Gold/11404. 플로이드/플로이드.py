import sys
input = sys.stdin.readline

n = int(input()) #도시
m = int(input()) #버스
INF = float('inf') 
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c= map(int,input().split())
    if graph[a][b]:
        graph[a][b] = min(graph[a][b],c)
    else:
        graph[a][b] = c

for k in range(1,n+1):
    graph[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j]=0
        print(graph[i][j],end=' ')
    print()