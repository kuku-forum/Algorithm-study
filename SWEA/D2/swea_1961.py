T = int(input())

def rot90(arr):
    return list(map(list, zip(*reversed(arr))))

def rot180(arr):
    return list(map(list, map(reversed, reversed(arr))))

def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]

for t in range(1, T+1):
    N = int(input())
    
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    board_90 =  [''.join(map(str, row)) for row in rot90(board)]
    board_180 = [''.join(map(str, row)) for row in rot180(board)]
    board_270 = [''.join(map(str, row)) for row in rot270(board)]
    
    print(f'#{t}')
    for a, b, c in zip(board_90, board_180, board_270):
        print(a, b, c)