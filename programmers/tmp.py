'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.5MB)
테스트 4 〉	통과 (0.56ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.5MB)
테스트 7 〉	통과 (0.06ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.06ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.4MB)
테스트 11 〉	통과 (0.16ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
'''
from collections import defaultdict

def solution(str1, str2):
    
    dic_s1 = defaultdict(int)
    dic_s2 = defaultdict(int)
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    intersection = 0
    union = 0
    
    for start in range(0, len(str1)-1):
        word1 = str1[start:start+2]
        if word1.isalpha() and len(word1) == 2:
            dic_s1[word1] += 1
    
    for start in range(0, len(str2)-1):
        word2 = str2[start:start+2]
        if word2.isalpha() and len(word2) == 2:
            dic_s2[word2] += 1
            
    print(dic_s1)
    print(dic_s2)
    if not dic_s1 and not dic_s2:
        return 65536
    
    '''
    합집합 = s1 + s2 - 교집합
    '''
    for key_1 in dic_s1.keys():
        if key_1 in dic_s2:
            intersection += min(dic_s1[key_1], dic_s2[key_1])    
        union += dic_s1[key_1]
        
    for key_2 in dic_s2.keys():
        union += dic_s2[key_2]
    union -= intersection
    
    return int(intersection/union*65536)