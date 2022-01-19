T = int(input())

def solution(num):
    result = []
    exp_lst = [2, 3, 5, 7, 11]
    
    for exp in exp_lst:
        cnt = 0
        while True:
            if num % exp == 0:
               cnt += 1
            else:
                break
            num /= exp
                
        result.append(cnt)

    return result

for t in range(1, T + 1):
    answer = []
    answer = ' '.join(map(str, solution(int(input()))))
    print(f'#{t} {answer}')