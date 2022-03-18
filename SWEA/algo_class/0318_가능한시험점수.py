from my_package.hjtc import swea_tc # as print

        

for t in range(1, int(input()) + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    case_lst = [0 for _ in range(sum(num_lst) + 1)]
    answer = [0]
    
    for i in range(N):
        for j in range(len(answer)):
            ssum = num_lst[i] + answer[j]
            
            if case_lst[ssum] == 0:
                case_lst[ssum] = 1
                answer.append(ssum)
    
    print(f'#{t} {len(answer)}')
    # break
    