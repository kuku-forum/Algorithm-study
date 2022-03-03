T = int(input())

for t in range(1, T + 1):
    N = int(input())
    
    num_chk = [0 for _ in range(10)]
    
    for num in input():
        num_chk[int(num)] += 1
        
    max_num = -1
    max_cnt = -1
    
    for num, cnt in enumerate(num_chk):
        if cnt >= max_cnt:
            max_num = num
            max_cnt = cnt
            
    print(f'#{t} {max_num} {max_cnt}')