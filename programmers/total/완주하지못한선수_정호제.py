def solution(participant, completion):
    
    par_dict = {}
    
    for p_name in participant:
        if p_name in par_dict:
            par_dict[p_name] += 1
        else:
            par_dict[p_name] = 1
            
    
    for c_name in completion:
        par_dict[c_name] -= 1
        
        if 0 >= par_dict[c_name]:
            del(par_dict[c_name])
    return ''.join(par_dict)

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.23ms, 10.4MB)
테스트 4 〉	통과 (0.53ms, 10.4MB)
테스트 5 〉	통과 (0.48ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (49.57ms, 21.6MB)
테스트 2 〉	통과 (40.76ms, 25.2MB)
테스트 3 〉	통과 (63.95ms, 27.5MB)
테스트 4 〉	통과 (64.45ms, 33.9MB)
테스트 5 〉	통과 (63.56ms, 33.9MB)
'''
from collections import defaultdict

def solution(participant, completion):
    parti_dict = defaultdict(int)
    
    for person in participant:
        parti_dict[person] += 1
        
    for person in completion:
        parti_dict[person] -= 1
        
        if parti_dict[person] == 0:
            del parti_dict[person] 
            
    
    return list(parti_dict)[0]