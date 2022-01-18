'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.38ms, 10.3MB)
테스트 7 〉	통과 (0.51ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (0.25ms, 10.2MB)
테스트 11 〉	통과 (0.17ms, 10.1MB)
테스트 12 〉	통과 (0.61ms, 10.2MB)
테스트 13 〉	통과 (0.34ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.70ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (145.04ms, 18.8MB)
테스트 2 〉	통과 (312.13ms, 27.2MB)
테스트 3 〉	통과 (1614.92ms, 64MB)
테스트 4 〉	통과 (126.10ms, 17.2MB)
테스트 5 〉	통과 (1783.29ms, 71.3MB)
'''
from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    
    heap = []
    for sco in scoville:
        heappush(heap, sco)
    
    
    while True:
        tmp1 = heappop(heap)    
        
        if tmp1 >= K:
            return answer
        else:
            if not heap:
                return -1
            else:
                heappush(heap, tmp1 + heappop(heap)*2)
                answer += 1