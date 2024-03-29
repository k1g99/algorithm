

import heapq
from collections import deque
from itertools import combinations

T = int(input())


def get_dist(s1, s2):
    a = abs(s1[0] - s2[0])
    b = abs(s1[1] - s2[1])
    return a + b

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    room = []
    stairs_cor = [] # [row, col, 깊이]
    people_cor = [] # [row, col]
    people_a = []  # [[stairA 까지 거리]]
    people_b = []  # [[stairB 까지 거리]]

    answer = 999999

    for r in range(N):
        row = list(map(int, input().split()))
        room.append(row)
        for c in range(N):
            if(row[c] == 1): # 사람 찾기
                people_cor.append([r,c])
            elif(row[c] > 1): # 계단찾기
                stairs_cor.append([r,c, row[c]])

    stair_a = stairs_cor[0][2]
    stair_b = stairs_cor[1][2]
    for p in people_cor:
        people_a.append(get_dist(stairs_cor[0], p))
        people_b.append(get_dist(stairs_cor[1], p))

    # 모든 조합 다 해보기
    comb = []
    people_num = len(people_cor)
    for i in range(0, people_num + 1):
        comb.append(list(combinations(range(len(people_cor)), i)))

    for cc in comb:
        for c in cc:
            arrive_a_pq = [] # [거리, 사람번호]
            arrive_b_pq = []
            for i in range(people_num):
                if (i in c): # A 계단으로
                    heapq.heappush(arrive_a_pq, [people_a[i], i])
                else : # B 계단으로
                    heapq.heappush(arrive_b_pq, [people_b[i], i])


            stair_a_que = deque() # [나오는 시간, Idx]
            stair_b_que = deque()
            h = 1
            while (arrive_a_pq or arrive_b_pq):
                # 계단 탈출 시켜추기
                while (stair_a_que and stair_a_que[0][0] == h):
                    stair_a_que.popleft()
                while (stair_b_que and stair_b_que[0][0] == h):
                    stair_b_que.popleft()

                # a
                while(arrive_a_pq and arrive_a_pq[0][0] == h): # hour 시간에 도착한 사람들에 대해서
                    top = heapq.heappop(arrive_a_pq)
                    if(len(stair_a_que) < 3): # stair 가 비어있으면 추가
                        stair_a_que.append([top[0] + stair_a, top[1]])
                    else:
                        top = [top[0] + 1, top[1]] # 아니면 +1 해서 다시 대기
                        heapq.heappush(arrive_a_pq, top)

                # b
                while (arrive_b_pq and arrive_b_pq[0][0] == h):  # hour 시간에 도착한 사람들에 대해서
                    top = heapq.heappop(arrive_b_pq)
                    if (len(stair_b_que) < 3):  # stair 가 비어있으면 추가
                        stair_b_que.append([top[0] + stair_b, top[1]])
                    else:
                        top = [top[0] + 1, top[1]]  # 아니면 +1 해서 다시 대기
                        heapq.heappush(arrive_b_pq, top)

                h += 1
            while (stair_a_que):
                hh = stair_a_que.popleft()
                h = max(hh[0], h)
            while (stair_b_que):
                hh = stair_b_que.popleft()
                h = max(hh[0], h)

            answer = min(h, answer)

    print(f"#{test_case} {answer+1}")
