'''
> 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명
> 감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명
> 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 

> 감독관 수의 최솟값
'''
import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = len(A)

for a in A:
    if a - B > 0:
        answer += math.ceil((a - B)/C)
    
print(answer)