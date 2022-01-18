
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.1MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.02ms, 10.1MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (13.46ms, 11.6MB)
테스트 2 〉	통과 (15.05ms, 11.4MB)
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
        
        if que2[-1] == '(' and tmp == ')':
            que2.pop()
        else:
            que2.append(tmp)
    
    return False if que2 else True
