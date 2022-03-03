from my_package.hjtc import swea_tc


T = int(input())


def check():
    # run * 2
    run_val = -2
    triplet = -2
    restore_list = []
    
    for i in range(8):
        if dp[i] > 0 and dp[i + 1] > 0 and dp[i + 2] > 0:
            dp[i] -= 1
            dp[i + 1] -= 1
            dp[i + 2] -= 1
            restore_list.extend([i, i + 1, i + 2])
            run_val += 1
            break
        
    for i in range(8):
        if dp[i] > 0 and dp[i + 1] > 0 and dp[i + 2] > 0:
            dp[i] -= 1
            dp[i + 1] -= 1
            dp[i + 2] -= 1
            restore_list.extend([i, i + 1, i + 2])
            run_val += 1
            break
    
    for restore in restore_list:
        dp[restore] += 1
    
    if run_val == 0:
        return 1
    
    # triplet * 2
    run_val = -2
    triplet = -2
    restore_list = []
    
    for i in range(10):
        if dp[i] >= 3:
            dp[i] -= 3
            restore_list.extend([i, i, i])
            triplet += 1
            break
        
    for i in range(10):
        if dp[i] >= 3:
            dp[i] -= 3
            restore_list.extend([i, i, i])
            triplet += 1
            break
        
    for restore in restore_list:
        dp[restore] += 1
    
    if triplet == 0:
        return 1
    
    
    # run, triplet
    run_val = -2
    triplet = -2
    restore_list = []
    
    for i in range(8):
        if dp[i] > 0 and dp[i + 1] > 0 and dp[i + 2] > 0:
            dp[i] -= 1
            dp[i + 1] -= 1
            dp[i + 2] -= 1
            restore_list.extend([i, i + 1, i + 2])
            run_val += 1
            break
    
    restore_list = []
    
    for i in range(10):
        if dp[i] >= 3:
            dp[i] -= 3
            restore_list.extend([i, i, i])
            triplet += 1
            break
        
    if run_val == -1 and triplet == -1:
        return 1
    
    return 0


for t in range(1, T + 1):
    answer = -1
    
    dp = [0 for _ in range(10)]
    num_lst = list(map(int, input()))
    
    for num in num_lst:
        dp[num] += 1
    
    swea_tc(f'#{t} {check()}')