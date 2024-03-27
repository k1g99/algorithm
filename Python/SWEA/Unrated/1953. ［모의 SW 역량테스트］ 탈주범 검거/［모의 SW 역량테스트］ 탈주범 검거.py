# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

#     상      하      좌      우
# [[-1,0], [1,0], [0,-1], [0,1]]

cell_type = {
    1:[[-1,0], [1,0], [0,-1], [0,1]],   # 상하좌우
    2:[[-1,0], [1,0]],   # 상하
    3:[[0,-1], [0,1]],   # 좌우
    4:[[-1,0], [0,1]],   # 상우
    5:[[1,0], [0,1]],    # 하우
    6:[[1,0], [0,-1]],   # 하좌
    7:[[-1,0], [0,-1]]   # 상좌
}

def checkBoundary(cr, cc):
    global N, M
    if(cr < 0 or cc < 0 or cr >= N or cc >= M):
        return False
    return True

def checkPossible(d, n_type): #d : 방향, n : next cell의 type
    if(d[0] == 0): # 좌우
        for nt in n_type:
            if(nt[1] + d[1] == 0):
                return True
    else: # 상하
        for nt in n_type:
            if(nt[0] + d[0] == 0):
                return True
    return False

def check(cr, cc): # [r,c] 에서 갈 수 있는 모든 cell 리턴
    global tunel
    curr_cell_type = cell_type[tunel[cr][cc]]
    ret = []

    for c in curr_cell_type:
        nr = cr + c[0]
        nc = cc + c[1]
        if(checkBoundary(nr, nc) and tunel[nr][nc]): # boundary 확인
            nxt_cell_type = cell_type[tunel[nr][nc]]
            if(checkPossible(c, nxt_cell_type)): # 다음 칸이 받을 수 있는지 확인
                ret.append([nr, nc])
    return ret


def bfs(r, c, max_dep):
    global visited, tunel, ans
    queue = deque()

    queue.append([r, c, 1]) #r, c, depth
    visited[r][c] = True

    while (queue):
        cr, cc, depth = queue.popleft()
        ans.append([cr, cc])
        if(depth >= max_dep): continue

        next_cells = check(cr, cc)
        for nc in next_cells:
            if(not visited[nc[0]][nc[1]]):
                queue.append([nc[0], nc[1], depth+1])
                visited[nc[0]][nc[1]] = True


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, R, C, hours = list(map(int, input().split()))    # 세로 크기 N, 가로 크기 M, 맨홀 위치 R C, 시간
    tunel = []
    ans = []

    for n in range(N):
        tunel.append(list(map(int, input().split())))

    visited = [[False for _ in range(M)] for _ in range(N)]
    bfs(R, C, hours)
    # print(ans)


    print(f"#{test_case} {len(ans)}")
