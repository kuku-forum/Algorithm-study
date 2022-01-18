'''
정확성  테스트
테스트 1 〉	통과 (8.65ms, 10.3MB)
테스트 2 〉	통과 (6.62ms, 10.2MB)
테스트 3 〉	통과 (4.82ms, 10.3MB)
테스트 4 〉	통과 (4.86ms, 10.2MB)
테스트 5 〉	통과 (7.34ms, 10.4MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (3.94ms, 10.3MB)
테스트 8 〉	통과 (2.74ms, 10.3MB)
테스트 9 〉	통과 (0.88ms, 10.3MB)
테스트 10 〉	통과 (8.95ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)
'''
from heapq import heappush, heappop

def solution(jobs):
    answer, now, cnt = 0, 0, 0
    heap = []
    start = -1
    
    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heappush(heap, [job[1], job[0]])
                
        if heap:
            min_job = heappop(heap)
            start = now
            now += min_job[0]
            answer += now - min_job[1]
            cnt += 1
        else:
            now += 1
    
    return answer // len(jobs)