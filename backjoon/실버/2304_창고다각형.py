N = int(input())


answer = 0
dp = [0 for _ in range(1002)]
fowd = [0 for _ in range(1002)]
back = [0 for _ in range(1002)]

for _ in range(N):
    L, H = map(int, input().split())
    dp[L] = H
    
f_val = dp[0]
b_val = dp[-1]

for i in range(1, 1002):
    j = 1001 - i
    
    if dp[i] > f_val:
        f_val = dp[i]
        
        
    if dp[j] > b_val:
        b_val = dp[j]
        
    fowd[i] = f_val
    back[j] = b_val

idx = 0
for i in range(idx, 1002):
    
    if fowd[i] == back[i]:
        idx = i
        break
    
    answer += fowd[i]
    
for i in range(idx, 1002):  
    answer += back[i]
    
print(answer)
    
    

    