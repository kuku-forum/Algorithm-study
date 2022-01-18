'''
정확성  테스트
테스트 1 〉	통과 (0.40ms, 10.3MB)
테스트 2 〉	통과 (0.51ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.12ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.3MB)
테스트 8 〉	통과 (0.73ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.14ms, 10.2MB)
테스트 11 〉	통과 (0.28ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.51ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.07ms, 10.3MB)
테스트 17 〉	통과 (0.34ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.41ms, 10.2MB)
테스트 20 〉	통과 (0.07ms, 10.2MB)
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque(list(map(list, zip([i for i in range(len(priorities))], priorities)))) 
    max_num = max(que, key = lambda x: x[1])[1]
    
    while True:
        num = que.popleft()

        if num[1] == max_num:
            answer += 1
            if num[0] == location:
                break
            max_num = max(que, key = lambda x: x[1])[1]
        else:
            que.append(num)
    
    return answer

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.16ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.07ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.06ms, 10.2MB)
테스트 20 〉	통과 (0.02ms, 10.2MB)
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque([[i, priority] for i, priority in enumerate(priorities)])
    priorities.sort()
    
    while que:
        node = que.popleft()
        
        if node[1] == priorities[-1]:
            if node[0] == location:
                return answer + 1
            else:
                priorities.pop()
                answer += 1
        else:
            que.append(node)