T = int(input())


for t in range(1, T+1):
    print(f'#{t}')
    

    
    N = int(input())
    if N == 1:
        dp = [[1]]
    else:
        dp = [[1], [1, 1]]
        
    if N > 2:
        for n in range(2, N):
            row = [1]
            
            for i in range(1, n):
                row.append(dp[n-1][i-1] + dp[n-1][i])
                
            row.append(1)
            dp.append(row)
        
    for row in dp:
        print(' '.join(map(str, row)))
        