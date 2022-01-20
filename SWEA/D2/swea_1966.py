T = int(input())

for t in range(1, T + 1):
    _ = input()
    arr = list(map(int, input().split()))
    arr.sort()
    answer = ' '.join(map(str, arr))
    print(f'#{t} {answer}')