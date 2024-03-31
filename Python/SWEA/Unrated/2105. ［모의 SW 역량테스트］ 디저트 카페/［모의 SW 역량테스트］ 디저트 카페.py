

T = int(input())

dir = [
    [1, 1], # 남동
    [1, -1],# 남서
    [-1, -1],# 북서
    [-1, 1]# 북동
]

def check_border(cell):
    global N
    r, c = cell
    if(r < 0 or c < 0 or r >= N or c >= N):
        return False
    return True

def dfs(start, path, dess):
    global check_paths
    i = 0
    nxt = [start[0] + dir[i][0], start[1] + dir[i][1]]
    if(check_border(nxt) and cafe[nxt[0]][nxt[1]] not in dess and path[-1] == 'r'):
            # new_dess = set()
            new_dess = dess.copy()
            new_dess.add(cafe[nxt[0]][nxt[1]])
            dfs(nxt, path + ['r'], new_dess)

    i = 1
    nxt = [start[0] + dir[i][0], start[1] + dir[i][1]]
    if (check_border(nxt) and cafe[nxt[0]][nxt[1]] not in dess):
        # new_dess = set()
        new_dess = dess.copy()
        new_dess.add(cafe[nxt[0]][nxt[1]])
        check_paths.append([nxt, path + ['l'], new_dess])
        dfs(nxt, path + ['l'], new_dess)


for test_case in range(1, T + 1):
    answer = -1

    N = int(input())
    cafe = []
    check_paths = []

    for r in range(N):
        row = list(map(int, input().split()))
        cafe.append(row)

    for r in range(N-2):
        for c in range(1, N-1):
            n = [r + dir[0][0], c + dir[0][1]]
            s = set()
            s.add(cafe[r][c])
            s.add(cafe[n[0]][n[1]])
            if(len(s) > 1):
                dfs(n, ['r'], s)

    for start, path, sets in check_paths:
        if(answer // 2 + 1 < len(sets)):
            path = path[:-1]
            isTrue = True
            for p in path:
                di = 2
                if(p == 'l'):
                    di = 3
                nxt = [start[0] + dir[di][0], start[1] + dir[di][1]]
                if(check_border(nxt)):
                    bef = len(sets)
                    # print(start, bef, nxt, sets)
                    sets.add(cafe[nxt[0]][nxt[1]])
                    if(bef + 1 != len(sets)):
                        isTrue = False
                        break
                    start = nxt
                else:
                    isTrue = False
                    break

            if(isTrue):
                answer = max(answer, len(sets))



    print(f"#{test_case} {answer}")
