from my_package.hjtc import swea_tc as print

def dfs(node):
    global answer
    
    if node > 0:
        answer += 1
        dfs(left[node])
        dfs(right[node])
    return

for t in range(1, int(input()) + 1):
    answer = 0
    E, N = map(int, input().split())
    
    left = [0 for _ in range(E + 2)]
    right = [0 for _ in range(E + 2)]
    
    num_lst = list(map(int, input().split()))
    
    for i in range(0, len(num_lst)-1, 2):
        if left[num_lst[i]] == 0:
            left[num_lst[i]] = num_lst[i+1]
        else:
            right[num_lst[i]] = num_lst[i+1]
    
    dfs(N)
    print(f'#{t} {answer}')