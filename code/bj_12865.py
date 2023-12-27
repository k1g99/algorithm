# 백준 12865q번 - 평범한 배낭
# https://www.acmicpc.net/problem/12865


# 가방 안에는 N개의 물건
# 물건 - W(무게), V(가치)
# 가방 안에 넣을 수 있는 물건들의 가치의 최댓값

# input: 
# N(물품 수), K(버틸 수 있는 무게)
# 각 물건의 무게 및 가치 (W V)

import sys

n, k = map(int, input().split())
item_list = [[0,0]]
result = 0
# dp[무게][idx]
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for _ in range(n):
    item_list.append(list(map(int, input().split())))

for weight in range(k+1):
    for idx in range(1, n+1, 1):    
        if (weight >= item_list[idx][0]): 
            dp[weight][idx] = max(dp[weight - item_list[idx][0]][idx - 1] + item_iist[idx][1])


result = dp[k][n]
print(result)