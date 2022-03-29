from my_package.hjtc import swea_tc

for t in range(1, int(input()) + 1):
    answer = 0
    N, M = map(int, input().split())
    w_lst = sorted(map(int, input().split()))
    truck_lst = sorted(map(int, input().split()))
    
    while truck_lst:
        truck = truck_lst.pop()
        
        while w_lst:
            w = w_lst.pop()
            
            if truck >= w:
                answer += w
                break
        else:
            break
            
    print(f'#{t} {answer}')
            
    