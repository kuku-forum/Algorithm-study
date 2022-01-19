T = int(input())

def solution(num_init):
    chk_lst = [False for _ in range(10)]
    chk_sum = 0
    cnt = 0
    num = 0
    
    while 10 > chk_sum:
        cnt += 1
        num = str(num_init * cnt)
        
        for n in num:
            if chk_lst[int(n)] == False:
                chk_lst[int(n)] = True
                chk_sum += 1
    return num

for t in range(1, T+1):
    answer = solution(int(input()))
    print(f'#{t} {answer}')