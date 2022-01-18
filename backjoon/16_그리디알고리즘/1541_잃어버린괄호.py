
nums = input().split('-')
answer = 0

for i in nums[0].split('+'):
    answer += int(i)

for num in nums[1:]:
    for i in num.split('+'):
        answer -= int(i)

print(answer)


#syntax error가 발생하는 이유를 모르겠음
T = input()
nums = T.split('-')
answer = eval(nums[0])

for num in nums[1:]:
    answer -= eval(num)

print(answer)


