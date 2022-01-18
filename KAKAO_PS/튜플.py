'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.07ms, 10.4MB)
테스트 5 〉	통과 (0.28ms, 10.4MB)
테스트 6 〉	통과 (1.73ms, 10.4MB)
테스트 7 〉	통과 (23.04ms, 11.7MB)
테스트 8 〉	통과 (105.24ms, 15.1MB)
테스트 9 〉	통과 (41.52ms, 12.4MB)
테스트 10 〉	통과 (121.25ms, 15.4MB)
테스트 11 〉	통과 (249.95ms, 17MB)
테스트 12 〉	통과 (490.11ms, 20.3MB)
테스트 13 〉	통과 (282.41ms, 20.1MB)
테스트 14 〉	통과 (478.02ms, 20.3MB)
테스트 15 〉	통과 (0.03ms, 10.4MB)
'''
from collections import deque

def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    
    num_list = []
    
    for num in s:
        num_list.append(num.split(','))
    
    num_list.sort(key = len)
    
    for num in num_list:
        for i in range(len(num)):         
            if int(num[i]) not in answer:
                answer.append(int(num[i]))
        
    return answer