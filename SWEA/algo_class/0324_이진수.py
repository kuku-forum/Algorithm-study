for t in range(1, int(input()) + 1):
    N, nums = input().split()
    answer = ''
    hex_dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,}
    
    for num in nums:
        if num.isdigit():
            answer += bin(int(num))[2:].zfill(4)
        else:
            answer += bin(int(hex_dic[num]))[2:].zfill(4)
    
    print(f'#{t}', answer)