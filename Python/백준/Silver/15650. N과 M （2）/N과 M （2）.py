
# 1 ~ N 중에서 중복 없이 M개 고른 수열

N, M = list(map(int, input().split()))
visited = [False] * (N + 1)
nums = []

def dfs(i):

    if(len(nums) == M):
        print(" ".join(map(str, nums)))
        return

    for j in range(i, N+1):
        if(visited[j]):
            continue

        visited[j] = True
        nums.append(j)
        dfs(j)
        nums.pop()
        visited[j] = False

dfs(1)