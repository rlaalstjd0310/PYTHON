from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

def fib(n):
    if n>=1:
        dp[1]=1
    if n>=2:
        dp[2]=1
    for i in range(3,n+1):
        dp[i]= dp[i-1]+dp[i-2]
    return dp[n]

def fibonacci(n):
    return n-2

print(fib(n),fibonacci(n))