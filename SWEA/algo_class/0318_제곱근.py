from my_package.hjtc import swea_tc as print
import math

for t in range(1, int(input()) + 1):
    N = int(input())
    
    answer = -1
    num = pow(N, 1/3)
    
    if math.isclose(pow(num, 3), N):
        answer = int(num)
    
    print(f'#{t} {answer}')
    