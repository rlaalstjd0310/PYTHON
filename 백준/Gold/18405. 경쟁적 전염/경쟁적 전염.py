from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(n)]
s,x,y = map(int,input().split())

v = []
for i in range(n):
    for j in range(n):
        if m[i][j] != 0:
            v.append((m[i][j],0,i,j))

v.sort()

queue = deque(v)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    v,time,px,py = queue.popleft()
    if time == s:
        break

    for i in range(4):
        nx,ny = px +dx[i],py+dy[i]

        if 0<=nx < n and 0 <= ny < n and m[nx][ny] == 0:
            m[nx][ny] = v
            queue.append((v,time+1,nx,ny))

print(m[x-1][y-1])