def solution(answers):
    
    p_1 = [1, 2, 3, 4, 5]
    p_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt_list = [0, 0, 0]
    max_cnt = -1
    answer = []
    
    for i in range(len(answers)):
        
        if answers[i] == p_1[i%len(p_1)]:
            cnt_list[0] += 1
            
        if answers[i] == p_2[i%len(p_2)]:
            cnt_list[1] += 1
            
        if answers[i] == p_3[i%len(p_3)]:
            cnt_list[2] += 1
    
    for i in range(len(cnt_list)):
        
        if not answer:
            max_cnt = cnt_list[i]
            answer.append(i+1)
            
        elif cnt_list[i] > max_cnt:
            for j in range(len(answer)):
                if cnt_list[i] > cnt_list[j]:
                    answer.pop(0)
                    
            max_cnt = cnt_list[i]
            answer.append(i+1)
            
        elif cnt_list[i] == max_cnt:
            answer.append(i+1)
            
    answer.sort
    return answer

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (2.25ms, 10.3MB)
테스트 8 〉	통과 (0.40ms, 10.3MB)
테스트 9 〉	통과 (2.21ms, 10.3MB)
테스트 10 〉	통과 (1.01ms, 10.3MB)
테스트 11 〉	통과 (2.21ms, 10.3MB)
테스트 12 〉	통과 (2.05ms, 10.4MB)
테스트 13 〉	통과 (0.12ms, 10.2MB)
테스트 14 〉	통과 (2.18ms, 10.4MB)
'''
def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    max_score = 0
    
    answer = []
    
    for name, p in enumerate([p1, p2, p3]):
        len_p = len(p)
        score = 0
        for i, ans in enumerate(answers):
            if ans == p[i%len_p]:
                score += 1
                
        if max_score == score:
            answer.append(name + 1)
            
        elif score > max_score:
            answer.clear()
            answer.append(name + 1)
            max_score = score
            
    return answer