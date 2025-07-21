import sys
input = sys.stdin.readline
x,y=map(int,input().split())
def convert_to_base(x,y):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=''
    if x==0:
        return '0'
    while x>0:
        result = digits[x % y] + result
        x //= y
    return result
print(convert_to_base(x,y))