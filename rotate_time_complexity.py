'''
N은 1000번, 10000번으로 설정

N*N board를 90(v1), 90(v2), 180, 270 도를 회전할때 시간 측정
10번을 진행하여 평균값을 구함

실험결과
# N, 90(v1), 90(v2), 180, 270
N = 1000,  0.153 0.018 0.013 0.019
N = 10000, 21.288 4.618 1.965 4.311


original
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]


    
90도 회전: list(map(list, zip(*reversed(arr))))

reversed(arr) -> O(1)
[7, 8, 9]
[4, 5, 6]
[1, 2, 3]

*reversed(arr)
unpack -> pack 벗겨내겠다.

zip(*reversed(arr))
zip(7, 4, 1) -> zip type

map(list, zip(*reversed(arr)))) # O(N)
-> list type으로 변환
[7, 4, 1],  [8, 5, 2],  [9, 6, 3]

list(map(list, zip(*reversed(arr))))

list([7, 4, 1],  [8, 5, 2],  [9, 6, 3])
list(a_list, b_list, c_list) O(N)

O(N) + O(N) => O(2N) => O(N)
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
'''

import time

def print_board(arr):
    for row in arr:
        print(row)
    print()

n = 1000
board = [[0 for _ in range(n)] for _ in range(n)]
N = len(board)

# 21.288 sec, O(N**2)
def rot90_v1(arr):
    N = len(arr)
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 먼저 만들기
    
    for i in range(N): # N
        for j in range(N): # N
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr
            
# 4.618sec, O(N) + O(N) = O(2*N) -> O(N)
def rot90_v2(arr):
    return list(map(list, zip(*reversed(arr))))

# 1.965, O(N)
def rot180(arr):
    return list(map(list, map(reversed, reversed(arr))))

# 4.311
def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]

# 10회 실험
end1, end2, end3, end4, end5 = 0, 0, 0, 0, 0

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

