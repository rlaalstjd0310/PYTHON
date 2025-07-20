i=int(input()) # 전체 가격
l=int(input()) # 개수
r = [] # 가격 * 개수 집합들

for a in range(l):
    x,y = map(int,input().split())
    r.append(x*y) # r에 각 가격들이 있음

k = sum(r)

if k == i:
        print("Yes")
else :
        print("No")