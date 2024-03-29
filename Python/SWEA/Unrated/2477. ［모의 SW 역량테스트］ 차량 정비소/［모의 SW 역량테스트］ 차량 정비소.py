# time 순으로 진행된다고, for문으로 하나하나 따질 필요 없음!!! (99% 는 다른 (효율적인)방법이 있음)

import heapq as hq

T = int(input())
for test_case in range(1, T + 1):
    answer = -1

    a_num, b_num, K, TAR_A, TAR_B = list(map(int, input().split()))
    a_delay = list(map(int, input().split()))
    b_delay = list(map(int, input().split()))
    p_arrive = list(map(int, input().split()))

    people = [] # people : [[시작시간, id], ]
    for i in range(K):
        people.append([p_arrive[i], i])
    people.sort()

    # 접수 이후 시간 계산
    people_a = [] # people_a : [[끝시간, 창구번호, id], ]
    a_start_time = [0] * a_num
    for p_time, p_id in people:
        a_id = -1
        if(p_time >= max(a_start_time)): a_id = 0
        elif(p_time < min(a_start_time)):
            for a_id in range(a_num):
                if(a_start_time[a_id] == min(a_start_time)):
                    break
        else:
            for a_id in range(a_num):
                if(a_start_time[a_id] <= p_time):
                    break
        t = max(p_time, a_start_time[a_id]) + a_delay[a_id]
        a_start_time[a_id] = t
        people_a.append([t, a_id, p_id])
    people_a.sort()

    b_start_time = [0] * b_num
    count = [[0 for _ in range(b_num)] for _ in range(a_num)]

    for p_time, a_id, p_id in people_a:
        b_id = -1
        if(p_time >= max(b_start_time)): b_id = 0
        elif (p_time < min(b_start_time)):
            for b_id in range(b_num):
                if (b_start_time[b_id] == min(b_start_time)):
                    break
        else:
            for b_id in range(b_num):
                if(b_start_time[b_id] <= p_time):
                    break
        t = max(p_time, b_start_time[b_id]) + b_delay[b_id]
        b_start_time[b_id] = t
        count[a_id][b_id] += p_id + 1

    if(count[TAR_A-1][TAR_B-1]): answer = count[TAR_A-1][TAR_B-1]
    print(f"#{test_case} {answer}")