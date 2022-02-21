from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    info.reverse()
    
    max_diff = -1
    
    appech_score = 0
    ryan_score = 0
    
    ryan_info = [0 for _ in range(11)]
    score_list = [i for i in range(11)]
    a= [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]
    a.reverse()
    for combi_re in combinations_with_replacement(score_list, n):
        for num in combi_re:
            ryan_info[num] += 1
        
        
        for score in range(11):
            # if ryan_info == a:
            #     print(score, info[score], ryan_info[score])
                
            if info[score] >= ryan_info[score]:
                if info[score] > 0:
                    appech_score += score
            else:
                if ryan_info[0] > 0:
                    ryan_score += score
           
        cur_diff = ryan_score - appech_score
        
        # if ryan_info == a:
        #     print(info)
        #     print(ryan_info)
        #     print(ryan_score, appech_score)
        #     print()
        
        if  cur_diff > max_diff:
            print(ryan_info)
            max_diff = cur_diff
            answer = ryan_info
            
        ryan_info = [0 for _ in range(11)]
        appech_score = 0
        ryan_score = 0
    
    return answer[::-1]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2]

[0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 0]

'''