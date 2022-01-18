T = int(input())

for i in range(1, T+1):
    sum_num = 0
    for num in map(int, input().split()):
        sum_num += num
        
    print(f'#{i} {round(sum_num/10)}')