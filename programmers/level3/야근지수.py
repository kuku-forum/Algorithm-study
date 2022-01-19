'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.85ms, 10.2MB)
테스트 9 〉	통과 (0.69ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (735.80ms, 10.4MB)
테스트 2 〉	통과 (744.82ms, 10.4MB)
'''
import heapq

def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))

    for _ in range(n):
        max_num = heapq.heappop(heap)[-1]
        if max_num > 0:
            max_num -= 1
        heapq.heappush(heap, (-max_num, max_num))

    return sum(num[-1]**2 for num in heap)
