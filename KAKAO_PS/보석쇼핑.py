
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.09ms, 10.3MB)
테스트 3 〉	통과 (0.25ms, 10.4MB)
테스트 4 〉	통과 (0.27ms, 10.2MB)
테스트 5 〉	통과 (0.42ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.45ms, 10.2MB)
테스트 9 〉	통과 (0.78ms, 10.3MB)
테스트 10 〉	통과 (0.51ms, 10.3MB)
테스트 11 〉	통과 (0.82ms, 10.4MB)
테스트 12 〉	통과 (1.42ms, 10.4MB)
테스트 13 〉	통과 (2.20ms, 10.7MB)
테스트 14 〉	통과 (1.37ms, 10.5MB)
테스트 15 〉	통과 (4.36ms, 11.1MB)
효율성  테스트
테스트 1 〉	통과 (5.88ms, 11.4MB)
테스트 2 〉	통과 (7.18ms, 11.4MB)
테스트 3 〉	통과 (17.95ms, 14.3MB)
테스트 4 〉	통과 (9.80ms, 12MB)
테스트 5 〉	통과 (25.62ms, 16.9MB)
테스트 6 〉	통과 (36.12ms, 18.3MB)
테스트 7 〉	통과 (36.19ms, 20MB)
테스트 8 〉	통과 (41.13ms, 21.1MB)
테스트 9 〉	통과 (61.45ms, 23.7MB)
테스트 10 〉	통과 (98.45ms, 24.8MB)
테스트 11 〉	통과 (65.50ms, 25.7MB)
테스트 12 〉	통과 (44.20ms, 15.9MB)
테스트 13 〉	통과 (50.20ms, 20.5MB)
테스트 14 〉	통과 (110.37ms, 35.8MB)
테스트 15 〉	통과 (126.97ms, 35.2MB)
'''
from collections import defaultdict

def solution(gems):
    answer = []
    kind_gem = len(set(gems))
    dic_gem = defaultdict(int)
    count_gem = 0
    end = 0
    
    # start를 0부터 증가
    for start in range(len(gems)):
        
        # 보석종류보다 가진게 적을때, end가 범위를 넘지않을때까지 반복
        while kind_gem > count_gem and len(gems) > end:
            gem = gems[end]
            # dic을 확인하여 새로운 보석이 들어오면 하나를 더 간지것으로 간주
            if dic_gem[gem] == 0:
                count_gem += 1
            dic_gem[gem] += 1
            # end 증가
            end += 1
        
        # 종류와 가진보석이 같다고 판단하면 진행
        if kind_gem == count_gem :
            # 우선 시작점과 끝점 구간의 길이를 추가
            answer.append([start+1, end, end-start])
            # dic에서 시작점에 있는 보석 하나 제외
            dic_gem[gems[start]] -= 1
            # 시작점 보석이 0이되면 종류가 하나 없어지므로 카운트에서 1 뻄
            # 시작점이 하나씩 증가될테니 반복
            if dic_gem[gems[start]] == 0:
                count_gem -= 1
            
    answer.sort(key = lambda x: (x[2], x[0]))
    return [answer[0][0], answer[0][1]]