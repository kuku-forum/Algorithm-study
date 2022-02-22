for t in range(1, 11):
    N, nums = input().split()
    num_list = list(reversed(nums))
    
    answer = []
    print(num_list)
    while num_list:
        num = num_list.pop()
        if not answer:
            answer.append(num)
        elif answer[-1] == num:
            answer.pop()
        else:
            answer.append(num)
        
    print(f'#{t} {"".join(map(str, answer))}')