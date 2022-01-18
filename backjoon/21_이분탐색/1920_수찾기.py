# 아래와 시간복잡도 차이가 크지 않은것 같은데 시간 초과 발생
import sys

N = int(sys.stdin.readline())
N_list = sorted((map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
M_list = map(int, sys.stdin.readline().split())

for target in M_list:
    start = 0
    end = N-1
    break_trigger = True

    while True:
        mid = (start + end)//2

        # print('#1', N_list[mid], target, start, end, mid)
        if N_list[mid] == target:
            print(1)
            break_trigger = False
            break
        elif N_list[mid] < target:
            start = mid+1
        elif N_list[mid] > target:
            end = mid-1
        if start>end:
            # print('#2', N_list[mid], target, start, end, mid)
            break

    if break_trigger:
        print(0)

# import sys

# N = int(sys.stdin.readline())
# N_list = sorted((map(int, sys.stdin.readline().split())))

# M = int(sys.stdin.readline())
# M_list = map(int, sys.stdin.readline().split())

# for target in M_list:
#     start = 0
#     end = N-1

#     while True:
#         mid = (start + end)//2
#         if start == end:
#             if N_list[mid] == target:
#                 print(1)
#             else:
#                 print(0)
#             break

#         # print('#1', target, N_list[mid], start, end, mid)
#         if N_list[mid] == target:
#             print(1)
#             break
#         elif N_list[mid] < target:
#             start = mid+1
#         elif N_list[mid] > target:
#             end = mid-1
