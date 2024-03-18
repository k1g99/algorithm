from collections import deque

def solution(n, tops):
    # answer = 0
    
    nn = 2 * n + 1
    dp = [0 for _ in range(nn + 1)]
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    if(tops[0] == 1):
        dp[2] = dp[2] + dp[1]
    
    for i in range(3, nn + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
        if(i % 2 == 0 and tops[i//2 - 1] == 1):
            dp[i] = dp[i] + dp[i-1]
            dp[i] = dp[i] % 10007

    # print(dp)
    
    return dp[-1] % 10007