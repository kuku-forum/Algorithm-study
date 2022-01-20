T = int(input())

for t in range(1, T + 1):
    _ = input()
    a_lst = list(map(int, input().split()))
    
    max_a = max(a_lst)
    min_a = min(a_lst)
    
    print(f'#{t} {max_a - min_a}')