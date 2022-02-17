# from my_package.hjtc import swea_tc

for t in range(1, int(input()) + 1):
    
    str1 = set(input())
    str2 = input()
    alp_cnt = {}
    
    for alp in str2:
        if alp not in alp_cnt:
            alp_cnt[alp] = 1
        else:
            alp_cnt[alp] += 1
    
    max_cnt = -1
    for alp in str1:
        max_cnt = alp_cnt[alp] if alp_cnt[alp] > max_cnt else max_cnt
        
    print(f'#{t} {max_cnt}')
    