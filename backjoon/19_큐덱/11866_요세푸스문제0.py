'''
1234567
-> 3 6 2 7 5 1 4 
1234567 -> 3(2)
12x4567 -> 3(2) 6(4)
12x45x7 -> 3(2) 6(4) 2(1+5)
1xx45x7 -> 3(2) 6(4) 2(1+5) 7(3+4)
1xx45xx -> 3(2) 6(4) 2(1+5) 7(3+4) 5(2+3)
1xx4xxx -> 3 6 2 7 5 1
xxx4xxx -> 3 6 2 7 5 1 4
3 3 5 5 3 3
'''
import sys

N, K = map(int, sys.stdin.readline().split())
que = [i for i in range(1, N+1)]
i = 0
answer = []

while True:
    i += (K-1) 
    i %= (len(que))

    answer.append(str(que.pop(i)))
    if not que:
        break


print("<", ", ".join(answer), ">", sep='')