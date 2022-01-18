T = int(input())

for i in range(1, T+1):
    print(f'#{i} {max(map(int, input().split()))}')