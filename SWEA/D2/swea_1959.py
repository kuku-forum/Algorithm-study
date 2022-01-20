T = int(input())

def solution(n, m, A, B):
    max_val = -0xffff
    
    for start in range(m - n + 1):
        tmp_val = 0
        for i, j in enumerate(range(start, start + n)):
            tmp_val += A[i]*B[j]
        max_val = max(max_val, tmp_val)
        
    return max_val


for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    if M > N:
        answer = solution(N, M, arr1, arr2)
    else:
        answer = solution(M, N, arr2, arr1)
    print(f'#{t} {answer}')