
## 모든 경우의 수를 다 찾는 거!! -> 굳이 queue 써가면서 원소가 3개만 있는지 확인할 필요 없음! 

import heapq
from collections import deque
from itertools import combinations

T = int(input())

def cal_dist(a, b):
    t1 = abs(a[0] - b[0])
    t2 = abs(a[1] - b[1])
    return t1 + t2

for test_case in range(1, T + 1):
    ans = 9999
    N = int(input())

    p_cor = []
    p_dist = []
    s_cor = []
    s_dep = []
    room = []
    for r in range(N):
        row = list(map(int, input().split()))
        room.append(row)
        for c in range(N):
            if (row[c] == 1):
                p_cor.append([r,c])
            elif(row[c] > 1):
                s_cor.append([r,c])

    for p in p_cor:
        p_dist.append([cal_dist(p, s_cor[0]), cal_dist(p, s_cor[1])])

    # print(s_cor)
    for sc in s_cor:
        s_dep.append(room[sc[0]][sc[1]])

    p_num = len(p_cor)
    comb = []
    for i in range(p_num+1):
        temp = list(combinations(range(p_num), i))
        for t in temp:
            comb.append(t)


    for c in comb:
        arrive = [[], []]
        for i in range(p_num):
            if(i in c):
                arrive[0].append(p_dist[i][0] + s_dep[0])
            else:
                arrive[1].append(p_dist[i][1] + s_dep[1])

        arrive[0].sort()
        arrive[1].sort()

        len0 = len(arrive[0])
        len1 = len(arrive[1])
        if (len0 > 3):
            for i in range(3, len0):
                arrive[0][i] = max(arrive[0][i - 3] + s_dep[0], arrive[0][i])

        if (len1 > 3):
            for i in range(3, len1):
                arrive[1][i] = max(arrive[1][i - 3] + s_dep[1], arrive[1][i])

        m = 0
        if (arrive[0]):
            m = max(m, arrive[0][-1])
        if (arrive[1]):
            m = max(m, arrive[1][-1])

        ans = min(ans, m)

    print(f"#{test_case} {ans + 1}")


