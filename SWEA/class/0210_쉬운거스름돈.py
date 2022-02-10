from my_package.hjtc import swea_tc as print

T = int(input())

for t in range(1, T + 1):
    change_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = [0 for _ in range(len(change_lst))]
    money = int(input())
    
    for i, change in enumerate(change_lst):
        while money >= change:
            money -= change
            answer[i] += 1
    
    print(f'#{t}')
    print(f'{" ".join(map(str, answer))}')