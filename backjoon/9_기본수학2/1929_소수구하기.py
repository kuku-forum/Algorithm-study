import sys

N = list(map(int, sys.stdin.readline().split(' ')))

s_num = N[0]
e_num = N[1]

'''
1 2 -> 2
1 3 -> 2 3

2 3 -> 2 3

'''
answer = []


for num in range(s_num, e_num+1):
    end = int(num**0.5)+1
    if num == 1:
        continue
    if num == 2 or num == 3: 
        answer.append(num)
        continue
    for i in range(2, end):
        if num % i == 0:

            break
        if i == end-1:
            # print(num, i)
            answer.append(num)
    
for i in answer:
    print(i)