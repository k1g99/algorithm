# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

dir = [
    [-1, 0],    # up
    [0, 1],    # down
    [1, 0],    # right
    [0, -1]    # left
]

def checkBound(r, c):
    global N
    if(r < 0 or c < 0 or r >= N or c >= N):
        return False
    return True

def dfs(cr, cc, depth, cut):
    global ans, mount, visited, K
    ans = max(ans, depth)

    for d in range(4):
        nr = cr + dir[d][0]
        nc = cc + dir[d][1]

        if(checkBound(nr, nc)):
            if(visited[nr][nc] == 0):
                if(mount[nr][nc] < mount[cr][cc]):
                    visited[nr][nc] = 1
                    dfs(nr, nc, depth + 1, cut)
                    visited[nr][nc] = 0
                elif(mount[nr][nc] - K < mount[cr][cc] and cut > 0): # K값에 너무 크게 신경쓰지 않아도 된다!
                    temp = mount[nr][nc]
                    mount[nr][nc] = mount[cr][cc] - 1
                    visited[nr][nc] = 1
                    dfs(nr, nc, depth + 1, 0)
                    visited[nr][nc] = 0
                    mount[nr][nc] = temp




# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    mount = []
    top_height = 0
    top = []    # [(r, c), (r, c)]
    ans = 0
    visited = []

    for r in range(N):
        input_row = list(map(int, input().split()))
        mount.append(input_row)

        # top 찾기
        top_temp = max(input_row)
        if(top_height < top_temp):
            top_height = top_temp
            top = []

        for i, ir in enumerate(input_row):
            if(ir == top_height):
                top.append((r, i))
    # print(top)

    for t in top:
        r, c = t
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[r][c] = 1
        dfs(r, c, 1, 1)

    print(f"#{test_case} {ans}")
