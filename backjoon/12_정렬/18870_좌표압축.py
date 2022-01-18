import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums_sorted = sorted(set(nums))
nums_dict = {nums_sorted[i] : i for i in range(len(nums_sorted))}

for num in nums:
   print(nums_dict[num], end= ' ')
   
# print(nums_dict)
# answer = []

# for num in nums:
#     found = nums_sorted.index(num)
#     answer.append(str(found))

# print(' '.join(answer))




# while N != 0:
#     num = nums.pop(0)
#     found = nums_sorted.index(num)
#     print(found, end= ' ')
#     N -= 1

