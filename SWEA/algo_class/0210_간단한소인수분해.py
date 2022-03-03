T = int(input())

for t in range(1, 1 + T):
    case = int(input())
    answer = []
    
    num_lst = [2, 3, 5, 7, 11]
    
    for num in num_lst:
        tmp = 0
        while True:
            if case % num == 0:
                case = case // num
                tmp += 1
            else:
                break
        answer.append(tmp)
    
    answer_str = ' '.join(map(str, answer))
    print(f'#{t} {answer_str}')
    