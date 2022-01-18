'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.08ms, 10.3MB)
테스트 13 〉	통과 (0.07ms, 10.3MB)
테스트 14 〉	통과 (0.10ms, 10.3MB)
테스트 15 〉	통과 (0.11ms, 10.3MB)
테스트 16 〉	통과 (0.29ms, 10.3MB)
테스트 17 〉	통과 (0.25ms, 10.2MB)
테스트 18 〉	통과 (0.39ms, 10.3MB)
테스트 19 〉	통과 (0.56ms, 10.3MB)
테스트 20 〉	통과 (0.33ms, 10.3MB)
테스트 21 〉	통과 (0.33ms, 10.3MB)
테스트 22 〉	통과 (0.17ms, 10.3MB)
테스트 23 〉	통과 (0.49ms, 10.3MB)
테스트 24 〉	통과 (0.17ms, 10.3MB)
테스트 25 〉	통과 (0.30ms, 10.3MB)
'''

from collections import deque

def balanced_bracket(w):
    if not w:
        return '', ''
    
    chk = 0    
    for i, brk in enumerate(w):
        if brk == '(':
            chk += 1
        else:
            chk -= 1
            
        if chk == 0:
            return w[:i+1] , w[i+1:]

def right_bracket(w):
    que = deque(w)
    tmp = []
    tmp.append(que.popleft())
    while que:
        if tmp[-1] == '(' and que[0] == ')':
            tmp.pop()
            que.popleft()
        else:
            tmp.append(que.popleft())
    
    if not tmp:
        return True
    else:
        return False
    
    
def total_process(w):
    if not w:
        return ''
    
    u, v = balanced_bracket(w)
    
    if right_bracket(u):
        return u + total_process(v)
    
    else:
        tmp = '(' + total_process(v) + ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp

def solution(p):
    return total_process(p)