T = int(input())

def solution(num):
    
    operator = ['+', '-']
    idx = 0
    result = 0
    
    for n in range(1, num+1):
        if operator[idx] == '+':
            result += n    
        else:
            result -= n
            
        idx = (idx + 1)%2
    
    return result


for t in range(1, T + 1):
    print(f'#{t} {solution(int(input()))}')