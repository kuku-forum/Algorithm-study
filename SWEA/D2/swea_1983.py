T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    score_list = []
    answer = ''
    
    for n in range(1, N + 1):
        mid_score, fin_score, task = map(int, input().split())
        
        mid_score *= 0.35
        fin_score *= 0.45
        task *= 0.2
        total_score = mid_score + fin_score + task
        score_list.append([n, total_score])
        
    equal_num = N//10
    score_list.sort(key = lambda x: x[1])
    flag = False
    
    for score in ('A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'):
        for _ in range(equal_num):
            if score_list[-1][0] == K:
                flag = True
                answer = score
                break
            score_list.pop()
        
        if flag:
            break
        
    print(f'#{t} {answer}')