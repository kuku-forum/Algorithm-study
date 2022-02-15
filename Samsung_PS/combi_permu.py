M = 2
store_lst = [1, 2, 3]
print(store_lst)

def gen_product(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_product(arr, n - 1):
            result.append([elem] + C)
    return result

# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
print(gen_product(store_lst, M))


def gen_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i + 1:], n - 1):
            result.append([elem] + C)
            
    return result

# [[1, 2], [1, 3], [2, 3]]
print(gen_combi(store_lst, M))
'''
[1,2,3,4,5,6,7]

n= 3
[[1,2,3], [1,2,4]]
-> combi3을 다 뽑아내고 그다음 진행하는거
-> 복잡도가 높음

->[1,2,3]
'''

def gen_permu(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for P in gen_permu(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + P]

    return result

# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
print(gen_permu(store_lst, M))



def gen_combi_replace(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi_replace(arr[i:], n - 1):
            result.append([elem] + C)
    return result

print(gen_combi_replace(store_lst, M))
# [ [1, 2], [1, 3],  [2, 3], [3, 3]] -> combination
# -> combi replacement
# [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]] ->


def print_board(arr):
    for row in arr:
        print(row)
    print()

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def rotate90(arr):
    return list(map(list, zip(*reversed(arr))))
print_board(rotate90(board))

'''
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
'''


def arotate90(arr):
    return list(map(list, zip(*arr)))

print_board(arotate90(board))
'''
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

'''

'''
# 무한 루프
a = [1, 2, 3]
for i in a:
    print(i)
    a.append(4)
    
# RuntimeError: dictionary changed size during iteration
# dict 사이즈 에러
b = {1:2, 2:4, 3: 5}
for key in b.keys():
    print(b[key])
    b[4] = 6
    
# que 사이즈 에러
# RuntimeError: deque mutated during iteration
from collections import deque

que = deque([1, 2, 3, 4])
for q in que:
    print(q)
    que.append(5)
'''