import sys
input = sys.stdin.readline

x = int(input())
numbers = list(map(int,input().split()))

def count_num(n):
     count = 0
     for i in range(1,n+1):
          if n % i ==0:
               count+=1
     return count

num =[]


for l in numbers:
    if l != 1 and count_num(l) <=2:
         num.append(l)


print(len(num))