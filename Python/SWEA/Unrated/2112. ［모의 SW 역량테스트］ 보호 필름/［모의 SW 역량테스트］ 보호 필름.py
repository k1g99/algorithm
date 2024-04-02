
from itertools import combinations
from collections import deque

T = int(input())

def check(cov):
    global R, C, K

    if(K == 1):
        return True

    for c in range(C):
        find_from_col = False
        que = deque()
        r = 0
        for k in range(K):
            que.append(cov[r][c])
            r += 1
        if(not(0 in que and 1 in que)): # 연속된 3개 찾으면,
            continue
        for _ in range(K, R):
            que.popleft()
            que.append(cov[r][c])
            r += 1

            if (not (0 in que and 1 in que)):  # 연속된 3개 찾으면,
                find_from_col = True
                continue
        if(not find_from_col):
            return False

    return True

for test_case in range(1, T + 1):
    answer = 0
    R, C, K = list(map(int, input().split()))
    cover = []
    cover_init = []
    comb_all = [] # [[()], [(0,), (1,), (2,), (3,), (4,), (5,)], ,,, ]

    for r in range(R):
        row = list(map(int, input().split()))
        cover.append(row)
        cover_init.append(row)

    for k in range(K + 1):
        comb_all.append(list(combinations(range(R), k)))


    if(not check(cover)):
        answer = 99

        for comb_by_num in comb_all:
            # comb_by_num = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),,,]
            for cb in comb_by_num:
                ones = []
                for i in range(len(cb) + 1):
                    l = list(combinations(cb, i))
                    for ll in l:
                        ones.append(ll)

                for one in ones:
                    for c in cb: # cb : (0, 1)
                        if(c in one):
                            cover[c] = [1 for _ in range(C)]
                        else:
                            cover[c] = [0 for _ in range(C)]

                    if(check(cover)):
                        answer = len(cb)
                        break
                    else:
                        for c in cb:
                            cover[c] = cover_init[c]
                if (answer < 99):
                    break
            if(answer < 99):
                break

    print(f"#{test_case} {answer}")
