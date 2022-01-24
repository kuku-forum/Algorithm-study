

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    
    score_list = sorted(map(int, input().split()), reverse= True)
    answer = sum(score_list[:K])
    
    print(f'#{t} {answer}')
    
    