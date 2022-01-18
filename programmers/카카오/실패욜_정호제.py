'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (1.22ms, 10.6MB)
테스트 4 〉	통과 (6.34ms, 10.8MB)
테스트 5 〉	통과 (18.03ms, 15MB)
테스트 6 〉	통과 (0.20ms, 10.2MB)
테스트 7 〉	통과 (0.63ms, 10.2MB)
테스트 8 〉	통과 (6.32ms, 10.9MB)
테스트 9 〉	통과 (17.86ms, 15MB)
테스트 10 〉	통과 (12.33ms, 10.9MB)
테스트 11 〉	통과 (6.73ms, 11MB)
테스트 12 〉	통과 (10.28ms, 11.4MB)
테스트 13 〉	통과 (11.46ms, 11.5MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (4.30ms, 10.7MB)
테스트 16 〉	통과 (2.27ms, 10.4MB)
테스트 17 〉	통과 (8.35ms, 10.6MB)
테스트 18 〉	통과 (2.22ms, 10.4MB)
테스트 19 〉	통과 (0.48ms, 10.3MB)
테스트 20 〉	통과 (3.04ms, 10.4MB)
테스트 21 〉	통과 (8.57ms, 10.9MB)
테스트 22 〉	통과 (20.69ms, 18.4MB)
테스트 23 〉	통과 (14.47ms, 11.7MB)
테스트 24 〉	통과 (14.77ms, 11.7MB)
테스트 25 〉	통과 (0.01ms, 10.3MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.3MB)
'''
from collections import defaultdict

def solution(N, stages):
    non_clear = defaultdict(int)
    people = len(stages)
    fail_rate = []
    
    for stage in stages:
        non_clear[stage] += 1
    
    for i in range(1, N + 1):
        if non_clear[i] == 0 or people == 0:
            fail_rate.append([i, 0])    
        else:
            fail_rate.append([i, non_clear[i]/people])
            people -= non_clear[i]
    
    fail_rate.sort(key = lambda x: (-x[1], x[0]))
        
    return [idx[0] for idx in fail_rate]