# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

dir = [[-1,0], [1,0], [0,-1], [0,1]]

def change_dir(a):
    if (a == 0):
        return 1
    if (a == 1):
        return 0
    if (a == 2):
        return 3
    if (a == 3):
        return 2


def red_zone(r, c):
    global N
    if(r == 0 or c == 0 or r == N-1 or c == N-1):
        return True
    return False


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N 한 변의 셀의 개수 (5 ≤ N ≤ 100)
    # K 미생물 군집의 개수(5 ≤ K ≤ 1,000)
    # M 격리 시간 (1 ≤ M ≤ 1,000)
    # 상: 1, 하: 2, 좌: 3, 우: 4
    ans = 0
    N, M, K = list(map(int, input().split())) # N=7, M=2, K=9
    misc = dict()
    new_misc = dict()
    misc_cmp = dict()   # misc_cmp[(r, c)] = [[mn, md], [mn, md] ...

    for k in range(K):
        # 세로위치(1), 가로위치(1), 미생물 수(7), 이동방향(상)
        r, c, num, d = list(map(int, input().split()))
        misc[(r,c)] = [num, d-1]
    # print(misc)

    for _ in range(M):
        new_misc = {}
        misc_cmp = {}
        for m in misc:
            cr, cc = m
            mn, md = misc[m]

            nr = cr + dir[md][0]
            nc = cc + dir[md][1]

            if(red_zone(nr, nc)): # 레드존 -> 방향바꾸고, 반감
                mn = mn // 2
                md = change_dir(md)
                if(mn):
                    new_misc[(nr, nc)] = [mn, md]
            elif((nr, nc) in new_misc): # 이미 있으면 계산하고 합치기
                new_mn, new_md = new_misc[(nr, nc)]
                cmp_mn, cmp_md = misc_cmp[(nr, nc)]
                if(cmp_mn > mn):
                    new_misc[(nr, nc)] = [new_mn + mn, cmp_md]
                    misc_cmp[(nr, nc)] = [new_mn, new_md]
                else:
                    new_misc[(nr, nc)] = [new_mn + mn, md]
                    misc_cmp[(nr, nc)] = [mn, md]

            else: # 아니면 그냥 이동만 하기
                new_misc[(nr, nc)] = [mn, md]
                misc_cmp[(nr, nc)] = [mn, md]

        misc = new_misc

    for m in misc:
        ans += misc[m][0]

    print(f"#{test_case} {ans}")
