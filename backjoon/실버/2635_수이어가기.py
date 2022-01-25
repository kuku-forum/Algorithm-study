num1 = int(input())
answer = 0
answer_list = []

for num2 in range(1, num1 + 1):
    dp = [num1, num2]
    
    while dp[-2] >= dp[-1]:
        dp.append(dp[-2] - dp[-1])
        
    if len(dp) > answer:
        answer = len(dp)
        answer_list = dp
        
print(answer)
print(' '.join(map(str, answer_list)))
    