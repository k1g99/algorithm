# 백준 1655번 - 가운데를 말해요
# https://www.acmicpc.net/problem/1655


# input: 
# N (정수의 개수) (1 <= N <= 100,000)

from heapq import heappush, heappop

N = int(input())

minPQ = [] # 기본적으로 heapq는 minHeap 
maxPQ = [] # (-num, num)으로 추가해서 사용하기

nums = [int(input()) for _ in range(N)]

# maxPQ, minPQ
for n in nums:
    if len(maxPQ) == len(minPQ):
        heappush(maxPQ, (-n, n))
    else:
        heappush(minPQ, n)

    # root값들끼리 비교해서 MaxPQ의 값이 더 크면 서로 바꾸기
    if minPQ and (maxPQ[0][1] > minPQ[0]):
        left = heappop(maxPQ)[1]
        right = heappop(minPQ)

        heappush(maxPQ, (-right, right))
        heappush(minPQ, left)
    
    print(maxPQ[0][1])