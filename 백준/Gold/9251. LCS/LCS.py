import sys
input = sys.stdin.readline
n = list(input().strip())
m = list(input().strip())

def lcs(x,y):
    n,m = len(x),len(y)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]
    
print(lcs(n,m))