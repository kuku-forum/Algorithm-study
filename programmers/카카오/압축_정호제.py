'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.37ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.33ms, 10.2MB)
테스트 7 〉	통과 (0.26ms, 10.2MB)
테스트 8 〉	통과 (0.29ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.50ms, 10.3MB)
테스트 11 〉	통과 (0.22ms, 10.3MB)
테스트 12 〉	통과 (0.34ms, 10.3MB)
테스트 13 〉	통과 (0.47ms, 10.3MB)
테스트 14 〉	통과 (0.47ms, 10.3MB)
테스트 15 〉	통과 (0.45ms, 10.3MB)
테스트 16 〉	통과 (0.37ms, 10.3MB)
테스트 17 〉	통과 (0.30ms, 10.2MB)
테스트 18 〉	통과 (0.11ms, 10.4MB)
테스트 19 〉	통과 (0.14ms, 10.3MB)
테스트 20 〉	통과 (0.29ms, 10.3MB)
'''

def solution(msg):
    alp_dic = {chr(alp): num for alp, num in zip(range(ord('A'), ord('Z') + 1), range(1, 27))}
    
    start = 0
    end = 1
    add_num = 27
    answer = []
    
    while len(msg) + 1 > end:
        if msg[start:end] in alp_dic:
            end += 1
        else:
            alp_dic[msg[start:end]] = add_num
            add_num += 1
            answer.append(alp_dic[msg[start:end-1]])
            start = end - 1
    else:
        answer.append(alp_dic[msg[start:end-1]])
            
    return answer