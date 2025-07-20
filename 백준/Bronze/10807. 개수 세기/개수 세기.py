t= int(input()) # 몇개 받는지
n=map(int,input().split())
y=int(input())
f=0
for i in n:
     if i ==y:
          f+=1
print(f)