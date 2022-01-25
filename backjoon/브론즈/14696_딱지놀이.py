from collections import defaultdict

N = int(input())
a_dict = defaultdict(int)
b_dict = defaultdict(int)

# 별, 동그라미, 네모, 세모를 각각 숫자 4, 3, 2, 1
for _ in range(N):
    for i, tmp in enumerate(map(int, input().split())):
        if i == 0:
            continue
        a_dict[tmp] += 1
        
    for i, tmp in enumerate(map(int, input().split())):
        if i == 0:
            continue
        b_dict[tmp] += 1
    
    # print(a_dict)
    # print(b_dict)
    if a_dict[4] > b_dict[4]:
        print('A')
    elif a_dict[4] < b_dict[4]:
        print('B')
    
    elif a_dict[3] > b_dict[3]:
        print('A')
    elif a_dict[3] < b_dict[3]:
        print('B')
        
    elif a_dict[2] > b_dict[2]:
        print('A')
    elif a_dict[2] < b_dict[2]:
        print('B')
        
    elif a_dict[1] > b_dict[1]:
        print('A')
    elif a_dict[1] < b_dict[1]:
        print('B')
        
    else:
        print('D')
    a_dict.clear()
    b_dict.clear()