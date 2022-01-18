T = int(input())

for i in range(1, T+1):
    result = 0
    for num in map(int, input().split()):
        if num%2 != 0:
            result += num
            
    print(f'#{i} {result}')