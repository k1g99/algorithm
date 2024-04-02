
from collections import deque

C, R = list(map(int, input().split()))
mat = []
new_ones = deque() # [r, c, days]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상 하 좌 우

def check_bound(r, c):
    if(r < 0 or c < 0 or r >= R or c >= C):
        return False
    return True

def check_no_tomato(r, c):
    if(mat[r][c] == 0):
        return True
    return False

for r in range(R):
    row = list(map(int, input().split()))
    for c in range(C):
        if(row[c] == 1):
            new_ones.append([r, c, 0])
    mat.append(row)

answer = 0
while (new_ones):
    cr, cc, cd = new_ones.popleft()
    answer = max(answer, cd)
    for d in range(4): 
        nr, nc = cr + dir[d][0], cc + dir[d][1]
        if(check_bound(nr, nc) and check_no_tomato(nr, nc)):
            new_ones.append([nr, nc, cd + 1])
            mat[nr][nc] = 1

for r in range(R):
    for c in range(C):
        if(mat[r][c] == 0):
            answer = -1
            break
print(answer)



