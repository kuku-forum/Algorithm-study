'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (10.65ms, 11.5MB)
테스트 3 〉	통과 (12.93ms, 11.6MB)
테스트 4 〉	통과 (14.63ms, 11.5MB)
테스트 5 〉	통과 (12.74ms, 11.7MB)
테스트 6 〉	통과 (12.73ms, 11.6MB)
테스트 7 〉	통과 (12.80ms, 11.6MB)
테스트 8 〉	통과 (20.02ms, 11.5MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (132.13ms, 26.7MB)
테스트 2 〉	통과 (112.81ms, 26.7MB)
테스트 3 〉	통과 (121.42ms, 26.7MB)
테스트 4 〉	통과 (134.78ms, 26.7MB)
테스트 5 〉	통과 (121.71ms, 26.7MB)
테스트 6 〉	통과 (134.12ms, 26.8MB)
테스트 7 〉	통과 (134.89ms, 26.7MB)
테스트 8 〉	통과 (121.99ms, 26.7MB)
'''
from collections import deque

def solution(s):
    
    que1 = deque(list(s))
    que2 = deque([])
    
    while que1:
        tmp = que1.popleft()
        
        if not que2:
            que2.append(tmp)
            continue
        
        if que2[-1] == tmp:
            que2.pop()
        else:
            que2.append(tmp)
    
    if not que2:
        return 1
    else:
        return 0