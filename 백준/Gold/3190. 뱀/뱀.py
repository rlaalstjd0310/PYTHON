from collections import deque

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1

l = int(input())
turns = {}
for _ in range(l):
    t, d = input().split()
    turns[int(t)] = d

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0

snake = deque()
snake.append((1, 1))
time = 0
x, y = 1, 1

while True:
    time += 1
    dx, dy = dirs[dir_idx]
    nx, ny = x + dx, y + dy

    if nx < 1 or nx > n or ny < 1 or ny > n:
        break
    if (nx, ny) in snake:
        break

    snake.append((nx, ny))
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        snake.popleft()

    x, y = nx, ny

    if time in turns:
        if turns[time] == 'D':
            dir_idx = (dir_idx + 1) % 4
        else:
            dir_idx = (dir_idx - 1) % 4

print(time)
