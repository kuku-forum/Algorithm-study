for t in range(1, int(input()) + 1):
    N = int(input())//10
    dp = [1]
    
    for n in range(1, N + 1):
        
        if n%2 == 0:
            dp.append(dp[n - 1]*2 + 1)
            
        else:
            dp.append(dp[n - 1]*2 - 1)
            
    print(f'#{t} {dp[-1]}')
        