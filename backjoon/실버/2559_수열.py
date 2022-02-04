N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_val = -1000000000000000
sum_temp = []
temp = 0

for i in range(len(arr)):
    temp += arr[i]
    sum_temp.append(temp)
    
    if i == K - 1:
        max_val = temp
        
    if i >= K :
        max_val = max(max_val, temp - sum_temp[i - K])
        
print(max_val)