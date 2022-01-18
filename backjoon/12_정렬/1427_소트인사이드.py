import sys

str_nums = sys.stdin.readline().split()[0]
nums = list(map(lambda num: int(num), str_nums))

answer = sorted(nums, reverse=True)
print(''.join(list(str(i) for i in answer)))
