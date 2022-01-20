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
        for C in gen_product(arr[i:], n - 1):
            result.append([elem] + C)
    return result

print(gen_combi_replace(store_lst, M))
# [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]]


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