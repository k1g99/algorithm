R, C = list(map(int, input().split()))
mat = []
dir = [[-1, 0], [1,0], [0,1], [0, -1]]
answer = 0
visited = [[False for _ in range(C+2)] for _ in range(R+2)]
part_sum = 0
max_val = 0

def dfs(r, c, n, s):
    global answer
    # 이런 방식으로 가망없는 경우들을 미리 제거해주는 게 포인트인가봄!!!! 
    if(n == 0 and s + max_val * 3 < answer):
        return 
    if(n == 1 and s + max_val * 2 < answer):
        return 
    if(n == 2 and s + max_val * 1 < answer):
        return 
    if(n == 3):
        answer = max(answer, s)
        return

    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if(nr > 0 and nc > 0 and nr <= R and nc <= C and not visited[nr][nc]):
            if(n == 1):
                visited[nr][nc] = True
                dfs(r, c, n+1, s + mat[nr][nc])
                visited[nr][nc] = False 
            visited[nr][nc] = True
            dfs(nr, nc, n+1, s + mat[nr][nc])
            visited[nr][nc] = False

mat.append([0] * (C+2))
for r in range(R):
    row = [0]
    row += list(map(int, input().split()))
    max_val = max(max_val, max(row))
    row += [0]
    mat.append(row)
mat.append([0] * (C+2))

for r in range(1, R+1):
    for c in range(1, C+1):
        visited[r][c] = True
        dfs(r, c, 0, mat[r][c])
        visited[r][c] = False


print(answer)