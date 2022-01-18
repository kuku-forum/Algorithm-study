nums = int(input())
factors = []
val_list = []
for _ in range(nums):
    factors.append(list(map(int, input().split())))
    val_list.append(1)
    

for one in range(nums):
    for other in range(nums):
        if one == other: continue
        
        if factors[one][0] < factors[other][0] and factors[one][1] < factors[other][1]:
            val_list[one] += 1
    
print(' '.join(list(str(i) for i in val_list)))

# import sys
# N = int(sys.stdin.readline())

# arr_x = []
# arr_y = []

# for i in range(N):
#     x, y = sys.stdin.readline().split()
#     x = int(x)
#     y = int(y)
#     arr_x.append(x)
#     arr_y.append(y)

# score = list(range(len(arr_x)))

# for i in range(len(arr_x)):
#     score[i] = 0
#     for j in range(len(arr_x)):
#         if arr_x[i] > arr_x[j] and arr_y[i] > arr_y[j]:
#             score[i] = score[i]-1
# print(score)

# sort_s = list(set(score))
# sort_s.sort()

# temp = [1]
# for i in range(1,len(sort_s)):
#     temp.append(score.count(sort_s[i-1])+i)

# rank = [temp[sort_s.index(x)] for x in score]

# print(' '.join(map(str, rank)))