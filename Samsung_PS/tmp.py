def print_board(arr):
    for row in arr:
        print(row)
    print()


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]

print_board(a)
b = rot270(a)
print_board(b)