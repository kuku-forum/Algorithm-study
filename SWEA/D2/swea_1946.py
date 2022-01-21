T = int(input())

for t in range(1, T + 1):
    N = int(input())
    answer = ''
    window = 10
    
    for _ in range(N):
        alp, num = input().split()
        for _ in range(int(num)):
            answer += alp
    
    print(f'#{t}')
    for i in range(0, len(answer), window):
        print(answer[i:i+window])