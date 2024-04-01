
from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    N, M, C = list(map(int, input().split()))
    all_comb = []

    for r in range(N):
        row = list(map(int, input().split()))

        for i in range(N - M + 1):
            pick = row[i:i+M]

            for j in range(1, M+1):
                comb = list(combinations(pick, j))
                for c in comb:
                    if(sum(c) <= C):
                        all_comb.append([sum(x**2 for x in c), [r, -1*i]])

    all_comb.sort(reverse=True)
    # isPicked = [[False for _ in range(N)] for _ in range(N)]
    #
    # cnt = 0
    # for sq, start in all_comb:
    #     r, c = start
    #     c *= -1
    #     if(isPicked[r][c]): continue
    #
    #     for m in range(M):
    #         isPicked[r][c + m] = True
    #
    #     answer += sq
    #     cnt += 1
    #     if(cnt == 2):
    #         break


    #### 문제 이상함!!!!!!
    isPicked = [False for _ in range(N)]

    cnt = 0
    for sq, start in all_comb:
        r, c = start
        if(isPicked[r]): continue
        isPicked[r] = True

        answer += sq
        cnt += 1
        if(cnt == 2):
            break

    print(f"#{test_case} {answer}")