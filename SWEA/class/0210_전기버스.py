from my_package.hjtc import swea_tc 

for t in range(int(input())):
    K, N, _ = map(int, input().split())
    charge_list = [0 for _ in range(N)]
    
    for charge in map(int, input().split()):
        charge_list[charge] = 1
    
    answer = 0
    
    pos = 0
    while pos + K < N:
        flag = True
        for i in range(K + pos , pos, -1):
            if charge_list[i] == 1:
                pos = i
                flag = False
                answer += 1
                break
        if flag:
            answer = 0
            break
    
    print(f'#{t + 1} {answer}')