T = int(input())

name_num = 666

while T:
    if '666' in str(name_num):
        T -= 1
        print(name_num)
    name_num += 1
    
print(name_num-1)


# import sys
# N = int(sys.stdin.readline())

# num = list(range(N))
# arr= []
# for i in range(len(num)):
#     temp = [char for char in str(num[i])]
#     ad_num = []
#     for j in range(len(temp)+1):
#         temp_ad = temp.copy()
#         temp_ad.insert(j,'666')
#         ad_num.append(int(''.join(temp_ad)))

#     arr.extend(ad_num)
# arr = list(set(arr))
# arr.sort()

# print(arr[N-1])