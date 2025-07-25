import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
else:
    xs = ys = float('inf')
    xm = ym = float('-inf')

    for _ in range(n):
        x, y = map(int, input().split())
        xs = min(xs, x)
        xm = max(xm, x)
        ys = min(ys, y)
        ym = max(ym, y)

    lx = xm - xs
    ly = ym - ys
    print(lx * ly)