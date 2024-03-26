T = int(input())
INF = int(1e9)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    costs = list(map(int, input().split()))
    days = list(map(int, input().split()))
    # print(costs)
    # print(days)

    dp = [0] * 13

    for i in range(1, 13):
        temp = [0, 0, INF, INF]

        temp[0] = days[i-1] * costs[0] + dp[i - 1]
        temp[1] = costs[1]             + dp[i - 1]

        if(i >= 3):
            temp[2] = dp[i - 3] + costs[2]

        dp[i] = min(temp)

    # print(dp)
    print("#" + str(test_case) +" " + str(min(dp[-1], costs[3])))