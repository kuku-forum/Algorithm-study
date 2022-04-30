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
print()
print('gen_product', gen_product(store_lst, M))


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
print()
print('gen_combi', gen_combi(store_lst, M))
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
print()
print('gen_permu', gen_permu(store_lst, M))



def gen_combi_replace(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi_replace(arr[i:], n - 1):
            result.append([elem] + C)
    return result

print()
print('gen_combi_replace', gen_combi_replace(store_lst, M))
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

def rot90(arr):
    return list(map(list, zip(*reversed(arr))))
print()
print('rotate 90')
print_board(rot90(board))

def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]

print('rot 270')
print_board(rot270(board))


# 1.965, O(N)
def rot180(arr):
    return list(map(list, map(reversed, reversed(arr))))

print('rot 180')
print_board(rot180(board))





