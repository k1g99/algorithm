import heapq

def solution(coin, cards):
    answer = 0
    hq = []
    n = len(cards)
    cost = [1 for _ in range(n+1)]
    pair = [0 for _ in range(n//2 + 1)]
    
    # 처음 패 초기화
    for i in range(n//3):
        num = cards[i]
        cost[num] = 0
        
        _num = num
        if(num > n//2):
            _num = n + 1 - num
        pair[_num] += 1
        
        if (pair[_num] == 2):
            heapq.heappush(hq, 0)
            
    # round 시작
    i = n // 3
    j = i + 1

    def check_card(x):
        num = cards[x]
        if(num > n//2):
            num = n + 1 - num
        pair[num] += 1
        
        if (pair[num] == 2):
            c = cost[num] + cost[n + 1 - num]
            heapq.heappush(hq, c)
    
    for r in range(n // 2 - 1):
        answer = r + 1
        if(i >= n):
            break
            
        check_card(i)
        i += 2
        check_card(j)
        j += 2

        if(len(hq) == 0):
            break
        
        cc = heapq.heappop(hq)
        if(cc > coin):
            break
        
        coin -= cc
        
    return answer