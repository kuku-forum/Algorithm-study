'''
N*N board를 90_v1, 90_v2, 180, 270 도를 회전할때 속도 측정
10 번을진행하여 평균값을 구함

90_v1: N^2
90_v2: N
N = 1000,  0.143 0.018 0.013 0.019
N = 10000, 22.879 4.618 1.965 4.311
'''

import time

n = 1000
board = [[0 for _ in range(n)] for _ in range(n)]
N = len(board)

# 22.879 
def rot90_v1(arr):
    new_row_list90 = []
    for j in range(N):
        new_row_list90.append([])
        
        for i in range(N-1, -1, -1):
            new_row_list90[j].append(arr[i][j])
    # N**2
    return new_row_list90
            
# 4.618 
def rot90_v2(arr):
    return list(map(list, zip(*reversed(arr))))

# 1.965 
def rot180(arr):
    return list(map(list, map(reversed, reversed(arr))))

    # return list(map(list, O(1)))
    # return list(O(N))
    # return 2*O(N)
    

# 4.311
def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]

end1, end2, end3, end4 = 0, 0, 0, 0

for _ in range(10):
    start1 = time.time()  
    a = rot90_v1(board)
    end1 += (time.time() - start1)

    start2 = time.time()
    a = rot90_v2(board)
    end2 += (time.time() - start2)

    start3 = time.time()  
    a = rot180(board)
    end3 += (time.time() - start3)

    start4 = time.time()  
    a = rot270(board)
    end4 += (time.time() - start4)
    
print(round(end1/10, 3), round(end2/10, 3), round(end3/10, 3), round(end4/10, 3))
