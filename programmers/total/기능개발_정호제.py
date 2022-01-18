from collections import deque

def solution(progresses, speeds):
    answer = []
    pro = deque(progresses)
    sp = deque(speeds)
    
    while pro:
        
        if pro[0] >= 100:
            cnt = 0
            
            while pro and pro[0] >= 100:  
                pro.popleft()
                sp.popleft()
                cnt += 1
            answer.append(cnt)
        
        else:
            for i in range(len(pro)):
                pro[i] += sp[i]
    
    return answer

#%%
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.32ms, 10.3MB)
테스트 3 〉	통과 (0.42ms, 10.3MB)
테스트 4 〉	통과 (0.15ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.37ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.30ms, 10.2MB)
테스트 10 〉	통과 (0.30ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
'''

from collections import deque

def solution(progresses, speeds):
    que_pro = deque(progresses)
    que_spe = deque(speeds)
    answer = []
    
    while que_pro:
        for i, speed in enumerate(que_spe):
            que_pro[i] += speed
        
        cnt = 0
        while que_pro and que_pro[0] >= 100:
            que_pro.popleft()
            que_spe.popleft()
            cnt += 1
        else:
            if cnt:
                answer.append(cnt)
            
    return answer