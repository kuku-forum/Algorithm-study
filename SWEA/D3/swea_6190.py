T = int(input())

for t in range(1, T + 1):
    answer = -1
    N = int(input())
    num_lst = sorted(map(int, input().split()), reverse = True)
    flag = False
    
    for i in range(N):
        for j in range(i + 1, N):
            tmp = num_lst[i]*num_lst[j]
            if answer > tmp:
                break
            mul_num = str(tmp)
            
            if len(mul_num) == 1:
                continue
            
            sort_mul_num = ''.join(sorted(mul_num))
            
            if mul_num == sort_mul_num:
                answer = max(answer, int(mul_num))
                        
    print(f'#{t} {answer}')