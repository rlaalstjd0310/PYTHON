from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = [list(input().split()) for _ in range(n)]
t = []
empty = []
for i in range(n):
    for j in range(n):
        if m[i][j] == "T":
            t.append((i, j))
        elif m[i][j] == "X":
            empty.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(len(empty)):
    for j in range(i+1, len(empty)):
        for k in range(j+1, len(empty)):
            for x, y in [empty[i], empty[j], empty[k]]:
                m[x][y] = 'O'

            ok = True
            for x, y in t:
                for d in range(4):
                    nx, ny = x, y
                    while True:
                        nx += dx[d]
                        ny += dy[d]
                        if not (0 <= nx < n and 0 <= ny < n):
                            break
                        if m[nx][ny] == 'O':
                            break
                        if m[nx][ny] == 'S':
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break

            if ok:
                print("YES")
                sys.exit(0)

            for x, y in [empty[i], empty[j], empty[k]]:
                m[x][y] = 'X'

print("NO")
