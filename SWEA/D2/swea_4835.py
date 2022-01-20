T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    a_lst = list(map(int, input().split()))
    
    min_val = 10000*101 
    max_val = -0xffff
    
    for window in range(N - M + 1):
        num = sum(a_lst[window : window + M])
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        
    print(f'#{t} {max_val - min_val}')