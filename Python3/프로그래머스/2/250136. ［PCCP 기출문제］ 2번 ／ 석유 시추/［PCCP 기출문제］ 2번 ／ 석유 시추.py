from collections import deque

def solution(land): # 1 : 석유
    def checkBorder(_d, _w):
        if (_d < 0):
            return False
        if (_w < 0):
            return False
        if (_d >= deep):
            return False
        if (_w >= width):
            return False
        
        return True
    
    dir = [
        [-1, 0], # up
        [1, 0], # down
        [0, -1], # left 
        [0, 1] # right
    ]

    # 500 * 500 = 250000
    answer = 0
    
    deep = len(land)
    width = len(land[0])
    count_width = [0 for _ in range(width)]
    
    # dfs 진행 -> width 에 추가하기
    for i in range(deep):
        for j in range(width):
            if(land[i][j] == 0):
                continue
			
            check_width = set()
            check_oils = 0
            # 석유를 만났을 떄
            # dfs 진행
            stack = deque()
            stack.append([i, j])
            check_oils += 1
            check_width.add(j)
            land[i][j] = 0
            
            while (len(stack) > 0):
                ci, cj = stack.pop()
                for d in dir:
                    ni = ci + d[0]
                    nj = cj + d[1]
                	
                    if (checkBorder(ni, nj) and land[ni][nj] == 1):
                        stack.append([ni,nj])
                        check_oils += 1
                        check_width.add(nj)
                        land[ni][nj] = 0
                
            for cw in check_width:
                count_width[cw] += check_oils
            
    return max(count_width)

# 몇 번째 열인지는 중요하지 않음, 최대한 많은 양이면 됨