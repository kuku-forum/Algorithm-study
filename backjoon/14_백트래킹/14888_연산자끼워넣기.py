import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
opr_n = list(map(int, sys.stdin.readline().split()))
opr_str = '+'*opr_n[0] + '-'*opr_n[1] + '*'*opr_n[2] + '/'*opr_n[3]
opr_list = list(set(permutations(opr_str, len(opr_str))))
eval_list = []

for opr in opr_list:
    for i in range(len(nums)):
        if i == 0:
            tmp = nums[0]
        elif opr[i-1] == '+':
            tmp += nums[i]
        elif opr[i-1] == '-':
            tmp -= nums[i]
        elif opr[i-1] == '*':
            tmp *= nums[i]
        elif opr[i-1] == '/':
            if tmp >= 0:
                tmp //= nums[i]
            else:
                tmp = -(abs(tmp)//nums[i])
    
    eval_list.append(tmp)

print(max(eval_list))
print(min(eval_list))