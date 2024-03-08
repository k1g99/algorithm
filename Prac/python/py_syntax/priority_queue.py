from heapq import heapify, heappop, heappush

############## MIN HEAP ############## 
a = [4, 6, 2, 8, 10, 2, -99, 39]

heapify(a)
print(a)   # [-99, 6, 2, 8, 10, 2, 4, 39]
heappop(a) # -99
print(a)   # [2, 6, 2, 8, 10, 39, 4]


############## MAX HEAP ############## 
a = [4, 6, 2, 8, 10, 2, -99, 39]
maxHeap = []

for aa in a:
    heappush(maxHeap, (-aa, aa)) # 이런 식으로 MAX HEAP 사용 가능!

b = []
for (_, n) in maxHeap:
    b.append(n)

print(b)   # [39, 10, 2, 8, 6, 2, -99, 4]
heappop(b) # 39
print(b)   # [2, 10, -99, 8, 6, 2, 4]
