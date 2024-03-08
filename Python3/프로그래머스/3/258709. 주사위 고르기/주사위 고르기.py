from itertools import combinations


def solution(dice):
    def getScore(picks): # getScore((1,2))
        res = []
        # dice[0] : (1,2,3)
        # dice[1] : (a,b,c)
        # dice[2] : (ㄱ,ㄴ,ㄷ)
        
        for p in picks:
            if (len(res) > 0):
                temp = []
                for r in res:
                    for d in dice[p]:
                        temp.append(r + d)
                res = temp
            else:
                res = [x for x in dice[p]]
        
        dic = dict()
        
        for x in res:
            if(x in dic.keys()):
                dic[x] += 1
            else:
                dic[x] = 1
        
        return dic
      
    answer = []
    n = len(dice)
    dice_idx = [x for x in range(n)] # [0,1,2,3]
    
    a_pick = list(combinations(dice_idx, n//2))
    
    all_scores = []
        
    for pick in a_pick:
        all_scores.append(getScore(pick))
    # print(all_scores)
    
    
    na = len(a_pick)
    
    
    max_win = 0
    max_pick = []
    for ai in range(na):
        bi = na - ai - 1
        
        a_score = all_scores[ai]
        b_score = all_scores[bi]
        
        a_win = 0
        b_win = 0
        
        for a_key in a_score:
            for b_key in b_score:
                if(a_key > b_key):
                    a_win += b_score[b_key] * a_score[a_key]
        
        
        if(a_win > max_win):
            max_win = a_win
            max_pick = a_pick[ai]
        
        answer = [x+1 for x in max_pick]


#     # 비교
#     na = len(a_pick)
#     max_win = 0
#     max_pick = []
#     for ai in range(na // 2):
#         bi = na - ai - 1
        
#         all_comp = len(all_scores[ai])
#         a_win = 0
#         b_win = 0
        
#         for ii in range(all_comp):
#             for jj in range(all_comp):
#                 if (all_scores[ai][ii] > all_scores[bi][jj]):
#                     a_win += 1
#                 elif (all_scores[ai][ii] < all_scores[bi][jj]):
#                     b_win += 1
        
#         w_win = a_win
#         wi = ai
#         if(b_win > a_win):
#             w_win = b_win
#             wi = bi
            
        
#         if (w_win > max_win):
#             max_win = w_win
#             max_pick = a_pick[wi]
        
#         print(w_win)
        
#     answer = [x+1 for x in max_pick]
    
    return answer