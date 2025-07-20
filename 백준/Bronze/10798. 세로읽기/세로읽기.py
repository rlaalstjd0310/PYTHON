import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(5)]
rarr = []
max_len = max(len(row) for row in arr)

for i in range(max_len):
    for row in arr:
        if i < len(row):
            rarr.append(row[i])

print("".join(rarr))