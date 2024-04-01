from collections import deque

N, M = list(map(int, input().split()))

edge = {}
for i in range(N + 1):
    edge[i] = []

froms = [0 for _ in range(N + 1)]
zeros = deque()
ans = []

for m in range(M):
    a, b = list(map(int, input().split()))
    edge[a].append(b)

    froms[b] += 1

for f in range(1, N + 1):
    if(froms[f] == 0):
        zeros.append(f)

while (zeros):
    z = zeros.pop()
    ans.append(z)

    for target in edge[z]:
        froms[target] -= 1
        if(froms[target] == 0):
            zeros.append(target)

print(" ".join(map(str, ans)))