from my_package.hjtc import swea_tc #as print

def in_order(n):
    global cnt, root, root_half
    
    if n:
        in_order(left[n])
        if n == 1:
            root = cnt +1
        if n == N//2:
            root_half = cnt +1
            
        cnt += 1
        in_order(right[n])
    return

for t in range(1, int(input()) + 1):
    N = int(input())
    root = 0
    root_half = 0
    cnt = 0
    left = [0 for _ in range(N + 1)]
    right = [0 for _ in range(N + 1)]
    num_lst = [n for n in range(N, 1, -1)]
    
    for p in range(1, N+1):
        if not num_lst: break
        left[p] = num_lst.pop()
        
        if not num_lst: break
        right[p] = num_lst.pop()
        
    
    in_order(1)
    print(f'#{t}', root, root_half)