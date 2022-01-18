#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (0.11ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.09ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.08ms, 10.1MB)
테스트 14 〉	통과 (0.07ms, 10.1MB)
테스트 15 〉	통과 (0.09ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
'''
from bisect import bisect_left

def solution(citations):
    answer = 0
    left, right = 0, len(citations)
    citations.sort()
    
    while left <= right:
        mid = (left + right)//2
        
        down_h = bisect_left(citations, mid)
        up_h = len(citations) - down_h
        
        if up_h >= mid >= down_h:
            left = mid + 1
            answer = max(answer, mid)
        else:
            right = mid - 1
        
    return answer

#%%
'''
정확성  테스트
테스트 1 〉	통과 (2.22ms, 10.3MB)
테스트 2 〉	통과 (2.64ms, 10.2MB)
테스트 3 〉	통과 (4.27ms, 10.3MB)
테스트 4 〉	통과 (2.60ms, 10.3MB)
테스트 5 〉	통과 (2.48ms, 10.2MB)
테스트 6 〉	통과 (2.33ms, 10.3MB)
테스트 7 〉	통과 (2.17ms, 10.3MB)
테스트 8 〉	통과 (3.64ms, 10.2MB)
테스트 9 〉	통과 (1.89ms, 10.2MB)
테스트 10 〉	통과 (2.20ms, 10.2MB)
테스트 11 〉	통과 (2.36ms, 10.2MB)
테스트 12 〉	통과 (2.09ms, 10.2MB)
테스트 13 〉	통과 (2.36ms, 10.3MB)
테스트 14 〉	통과 (2.33ms, 10.2MB)
테스트 15 〉	통과 (2.38ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
'''
from bisect import bisect_left

def solution(citations):
    citations.sort()
    max_h = citations[-1]
    len_h = len(citations)
    
    for idx in range(max_h, -1, -1):
        h_lower = bisect_left(citations, idx)
        h_upper = len_h - h_lower
        
        if h_upper >= idx and idx >= h_lower:
            return idx