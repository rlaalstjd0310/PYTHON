from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))


lis = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            lis[i] = max(lis[i], lis[j] + 1)

lds = [1] * n
for i in range(n-1,-1,-1):
    for j in range(i,n):
        if a[i] > a[j]:
            lds[i] = max(lds[i],lds[j]+1)

max_len = 0
for i in range(n):
    max_len = max(max_len, lis[i] + lds[i] - 1)

print(max_len)