import sys
import math
input = sys.stdin.readline

paper = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for r in range(y - 1, y - 1 + 10):
        for c in range(x - 1, x - 1 + 10):
            paper[r][c] = 1

total_area = 0
for r in range(100):
    for c in range(100):
        if paper[r][c] == 1:
            total_area += 1

print(total_area)