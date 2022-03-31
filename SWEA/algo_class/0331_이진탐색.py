from my_package.hjtc import swea_tc

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = list(map(int, input().split()))
    
    answer = 0
    for b in B:
        start = 0
        end = len(A)-1
        prev = None
        cur = None
        
        while end >= start:
            mid = (start + end)//2
            
            if A[mid] == b:
                answer += 1
                break
            
            elif A[mid] < b:
                if prev != 'right_search':
                    start = mid+1
                    prev = 'right_search'
                else:
                    break
            
            elif A[mid] > b:
                if prev != 'left_search':
                    end = mid-1
                    prev = 'left_search'
                else:
                    break
                
    print(f'#{t} {answer}')