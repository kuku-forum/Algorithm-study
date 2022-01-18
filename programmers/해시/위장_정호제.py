def solution(clothes):
    clo_dic = {}
    answer = 1
    
    for clo in clothes:
        if clo[1] in clo_dic:
            clo_dic[clo[1]] += 1
        else:
            clo_dic[clo[1]] = 1
    
    for cnt in clo_dic.values():
        answer *= (cnt + 1)
            
    return answer - 1

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
'''
from collections import defaultdict

def solution(clothes):
    answer = 1
    clo_type = defaultdict(int)
    
    for _, clo in clothes:
        clo_type[clo] += 1
        
    for val in clo_type.values():
        answer *= (val + 1)
    
    return answer - 1