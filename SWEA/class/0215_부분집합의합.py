def sum_func(arr):
    result = 0
    for num in arr:
        result += num
        
    return result

def subset(N, K):
    num_list = [n for n in range(1, 13)]
    result = 0
    for i in range(1 << len(num_list)):
        tmp = []
        for j in range(len(num_list)):
            
            if i & (1<<j):
                tmp.append(num_list[j])
                
        if len(tmp) == N and sum_func(tmp) == K:
            result += 1
    return result


for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    
    print(f'#{t} {subset(N, K)}')