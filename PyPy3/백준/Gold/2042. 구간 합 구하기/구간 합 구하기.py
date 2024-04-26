# 세그먼트 트리!!!!

N, M, K = list(map(int, input().split(" ")))

class Node():
    def __init__(self):
        self.st = 0
        self.ed = 0
        self.val = 0

class SegmentTree():
    def __init__(self, a):
        self.nodes = [Node() for _ in range(4*N)]
        # 세그먼트 트리 node 개수
        # 높이 : ceil(log2(N)) -> log2(N) or log2(N) + 1
        # node 개수 : 2^(log2(N) + 1) * 2 ~ N * 2 * 2 = 4N
        self.arr = a
        self.where_idx = [0 for _ in range(N)] # arr에서 x 번째 값이 tree의 어디에 있는지 저장
        self._init(0, N, 1)
        
    def _init(self, left, right, idx):
        self.nodes[idx].st = left
        self.nodes[idx].ed = right
        mid = (left + right) // 2
        
        if(left == mid):
            self.nodes[idx].val = self.arr[mid]
            self.where_idx[left] = idx
            return self.nodes[idx].val

        self.nodes[idx].val = self._init(left, mid, self.l_child(idx)) + self._init(mid, right, self.r_child(idx))
        return self.nodes[idx].val

    def update(self, idx, new_val):
        # parent 따라가면서 값 갱신
        node_idx = self.where_idx[idx]
        delta = new_val - self.nodes[node_idx].val
        while(node_idx != 0):
            self.nodes[node_idx].val += delta
            node_idx = node_idx // 2

    def show(self, left, right, idx):
        # tree 돌면서 left, right 범위 내에 포함되는 값이면 더하기
        if(idx > 4*N):
            return 0
        
        if(right < self.nodes[idx].st or self.nodes[idx].ed < left):
            # print("0")
            return 0
        
        if(left <= self.nodes[idx].st and self.nodes[idx].ed <= right):
            # print("idx", idx)
            return self.nodes[idx].val
        
        return self.show(left, right, self.l_child(idx)) + self.show(left, right, self.r_child(idx))

    def l_child(self, i):
        return i*2

    def r_child(self, i):
        return i*2 + 1


temp = []
for _ in range(N):
    temp.append(int(input()))

st = SegmentTree(temp)

for _ in range(M+K):
    a, b, c = list(map(int, input().split(" ")))
    if(a == 1): # b번쨰를 c로 바꾸기
        st.update(b-1, c)
    else: #  b부터 c까지 합 출력하기
        print(st.show(b-1, c, 1))
