def solution(alp, cop, problems):
    answer = 0
    
    target_alp = alp
    target_cop = cop
    
    for a,c,_,_,_ in problems:
        target_alp = max(target_alp, a)
        target_cop = max(target_cop, c)
        
    if(target_alp == alp and target_cop == cop):
        return 0
    
    INF = 999999999
    dp = [[INF for i in range(target_cop+1)] for j in range(target_alp+1)]
    dp[alp][cop] = 0    
        
    for a in range(alp, target_alp + 1):            
        for c in range(cop, target_cop + 1):
            dp[a][c] = min(a + c - alp - cop, dp[a][c])
            
            for sa, sc, ja, jc, h in problems:
                if(a >= sa and c >= sc):
                    na = a + ja
                    nc = c + jc
                    if(na > target_alp): na = target_alp 
                    if(nc > target_cop): nc = target_cop
                    
                    dp[na][nc] = min(dp[a][c] + h, dp[na][nc])
    
    
    return dp[target_alp][target_cop]