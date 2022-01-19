T = int(input())

for _ in range(T):
    idx = input()
    score_list = [[i, 0] for i in range(101)]
    grading_list = list(map(int, input().split()))
    
    for score in grading_list:
        score_list[score][1] += 1
        
    score_list.sort(key = lambda x: (-x[1], -x[0]))
    answer = score_list[0][0]
    # print(answer)
    
    print(f'#{idx} {answer}')