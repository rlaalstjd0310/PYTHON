import sys
input = sys.stdin.readline
x=int(input())
line=1
sum=0
while x>sum + line:
    sum += line
    line +=1

count = x - sum

left=0
right=0

if line %2 == 0:
    left = line - (count-1)
    right = count
else:
    left = count
    right = line - (count-1)
print(f"{right}/{left}")