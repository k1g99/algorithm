
# 1 ~ N 중에서 중복 없이 M개 고른 수열

N, M = list(map(int, input().split()))
visited = [False] * (N + 1)
nums = []

def dfs():
    if(len(nums) == M):
        s = " ".join(map(str, nums))
        print(s)
        return

    for i in range(1, N+1):
        if(visited[i]):
            continue

        visited[i] = True
        nums.append(i)
        dfs()
        nums.pop()
        visited[i] = False

dfs()


