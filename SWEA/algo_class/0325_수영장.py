from my_package.hjtc import swea_tc    

for t in range(1, int(input()) + 1):
    
    fee_lst = list(map(int, input().split()))
    arr = [0]
    arr.extend(map(int, input().split()))
    dp = [0 for _ in range(13)]
    
    for m in range(13):
        
        if m == 1:
            dp[m] = min(arr[m]*fee_lst[0], fee_lst[1])
        elif arr[m] == 0:
            dp[m] = dp[m-1]
        elif m >= 2:
            dp[m] = min(arr[m]*fee_lst[0] + dp[m-1], fee_lst[1] + dp[m-1], fee_lst[2] + dp[m-3])
        else:
            dp[m] = min(arr[m]*fee_lst[0] + dp[m-1], fee_lst[1] + dp[m-1])
    else:
        answer = min(dp[-1], fee_lst[3])
    
    print(f'#{t} {answer}')