'''
정확성  테스트
테스트 1 〉	통과 (590.90ms, 10.2MB)
테스트 2 〉	통과 (563.08ms, 10.3MB)
테스트 3 〉	통과 (575.17ms, 10.1MB)
테스트 4 〉	통과 (544.81ms, 10.2MB)
테스트 5 〉	통과 (530.77ms, 10.3MB)
테스트 6 〉	통과 (570.54ms, 10.2MB)
테스트 7 〉	통과 (539.82ms, 10.2MB)
테스트 8 〉	통과 (576.66ms, 10.2MB)
테스트 9 〉	통과 (526.92ms, 10.4MB)
테스트 10 〉	통과 (520.80ms, 10.3MB)
테스트 11 〉	통과 (526.98ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
'''
from collections import deque
from copy import deepcopy

def chk_correct(tmp_que):
    bracket = {'[': ']', '(': ')', '{': '}'}
    chk_que = deque([])
    
    while tmp_que:
        tmp = tmp_que.popleft()

        if not chk_que:
            chk_que.append(tmp)
            continue

        if chk_que[-1] in bracket:
            if bracket[chk_que[-1]] == tmp:
                chk_que.pop()
            else:
                chk_que.append(tmp)
        else:
            chk_que.append(tmp)
            
    return 1 if not chk_que else 0

def solution(s):

    cnt = 0
    que = deque(list(s))
    
    for i in range(len(que)):
        
        if i > 0:
            que.append(que.popleft())
        
        tmp_que = deepcopy(que)
        cnt += chk_correct(tmp_que)
    
    return cnt