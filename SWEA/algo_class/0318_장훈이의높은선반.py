from my_package.hjtc import swea_tc  as print


def subset():
    result = 10000*20 + 1
    for i in range(1 << len(num_lst)):
        sub_sum = -B
        for j in range(len(num_lst)):
            
            if i & (1 << j):
                sub_sum += num_lst[j]
                
        if sub_sum >= 0:
            if sub_sum == 0:
                return 0
            if result > sub_sum:
                result = sub_sum
    return result
            
for t in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    num_lst = list(map(int, input().split()))
    
    print(f'#{t} {subset()}')