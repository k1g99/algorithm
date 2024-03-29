

import heapq as hq

T = int(input())
for test_case in range(1, T + 1):
    answer = 0

    # A 접수 / B 정비 / K 사람 수
    A, B, K, targetA, targetB = list(map(int, input().split()))
    a_time = list(map(int, input().split()))
    b_time = list(map(int, input().split()))
    arrive = list(map(int, input().split()))
    count = [[0 for i in range(B)] for j in range(A)]

    a_wait_pq = [] # 접수 대기자 ([ID])
    b_wait_pq = [] # 정비 대기자 ([대기 시작 시간, 접수창구, ID])
    a_pq = [i for i in range(A)] # 남아있는 접수 창구 pop해줌
    hq.heapify(a_pq)
    b_pq = [i for i in range(B)] # 남아있는 정비 창구 pop해줌
    hq.heapify(b_pq)
    a = [[-1, -1] for _ in range(A)] # [[시간, ID]]
    b = [[-1, -1, -1] for _ in range(B)] # [[시간, ID, 접수 창구]]

    user_id = 0
    out_user = 0
    for t in range(30000000):
        if(out_user >= K): break

        # 접수 대기 채우기
        while(user_id < K and arrive[user_id] == t):
            hq.heappush(a_wait_pq, user_id) # 고객번호가 낮은 순서대로
            user_id += 1

        # 접수 창구 정리
        for ai in range(A):
            # 접수 -1씩
            if(a[ai][0] > 0):
                a[ai][0] -= 1

        for ai in range(A):
            # 접수 -> 정비 대기로 채우기
            if(a[ai][0] == 0):
                hq.heappush(b_wait_pq, [t, ai, a[ai][1]]) # 먼저 기다리는 고객이 우선 -> 접수 창구번호가 작은 고객이 우선
                hq.heappush(a_pq, ai)
                a[ai] = [-1,-1]
        # 접수 대기 -> 접수 이동
        while(a_wait_pq and a_pq):
            a_changu = hq.heappop(a_pq)
            a_person = hq.heappop(a_wait_pq)
            a[a_changu] = [a_time[a_changu], a_person]

        for bi in range(B):
            # 정비 -1 씩
            if(b[bi][0] > 0):
                b[bi][0] -= 1

        for bi in range(B):
            # 정비 완료 -> count 작성
            if (b[bi][0] == 0):
                count[b[bi][2]][bi] += (b[bi][1] + 1)
                out_user += 1
                hq.heappush(b_pq, bi)
                b[bi] = [-1, -1, -1]
        # 정비 대기 -> 정비 이동
        while(b_wait_pq and b_pq):
            b_changu = hq.heappop(b_pq)
            _, ai, b_person = hq.heappop(b_wait_pq)
            b[b_changu] = [b_time[b_changu], b_person, ai]

    answer = count[targetA - 1][targetB - 1]
    if(answer == 0): answer = -1
    print(f"#{test_case} {answer}")