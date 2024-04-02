from collections import deque
import sys
input = sys.stdin.readline    # python 입력 시간 단축!

N, M = list(map(int, input().split()))
# edge = {n: [] for n in range(N + 1)}
edge = [[] for n in range(N + 1)]
from_count = [0] * (N + 1)
from_count[0] = -1
answer = []

for m in range(M):
    start, end = list(map(int, input().split()))
    
    edge[start].append(end)
    from_count[end] += 1

remove_node = deque()
for i in range(1, N + 1):
    if(from_count[i] == 0):
        remove_node.append(i)

while(remove_node):
    node = remove_node.popleft()
    answer.append(node)
    for to_node in edge[node]:
        from_count[to_node] -= 1
        if(from_count[to_node] == 0):
            remove_node.append(to_node)
        
# print(answer)
print(" ".join(map(str, answer)))
