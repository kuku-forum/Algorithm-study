
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.11ms, 10.2MB)
테스트 3 〉	통과 (3.98ms, 10.3MB)
테스트 4 〉	통과 (289.26ms, 14.2MB)
테스트 5 〉	통과 (413.15ms, 14.2MB)
테스트 6 〉	통과 (264.99ms, 14.3MB)
테스트 7 〉	통과 (546.77ms, 14.2MB)
테스트 8 〉	통과 (535.90ms, 14.2MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
'''
def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        people = sum(mid//time for time in times)
        # print(start, end, mid, people)
        
#         if people == n:
#             return mid
        
#         elif people > n:
#             end = mid - 1
#         else:
#             start = mid + 1
            
        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer