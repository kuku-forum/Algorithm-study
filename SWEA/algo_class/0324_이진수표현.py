for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    answer = "OFF"
    if all(list(map(int, bin(M)[2:].zfill(N)[-N:]))):
        answer = "ON"
    
    print(f'#{t}', answer)