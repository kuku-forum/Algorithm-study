from my_package.hjtc import swea_tc

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    
    chk_list = [False for _ in range(N + 1)]

    
    for turin in map(int, input().split()):
        chk_list[turin] = True
        
    unsubmit = [str(num) for num in range(1, N + 1) if chk_list[num] == 0]
    answer = ' '.join(unsubmit) 
    
    swea_tc(f'#{t} {answer}')