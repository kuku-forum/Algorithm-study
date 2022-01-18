import sys

N, M = map(int, sys.stdin.readline().split())

board_lst = []
answer = 0

for _ in range(N):
    board_lst.append(list(map(int, sys.stdin.readline().split())))

tetmino_dic = {
            0: [[1, 1, 1, 1]],
            1: [[1,1], [1,1]],
            2: [[1,0], [1,0], [1,1]],
            3: [[1,0], [1,1], [0,1]],
            4: [[1,1,1], [0,1,0]]
}

def rotate90(arr):
    return list(zip(*reversed(arr)))

def symmetry(arr):
    return [list(reversed(a)) for a in arr]


def conv(arr):
    global answer
    tmp = 0
    for s_i in range(N - len(arr) + 1):
        for s_j in range(M - len(arr[0]) + 1):
            
            for i in range(len(arr)):
                for j in range(len(arr[0])):                    
                    tmp += arr[i][j] * board_lst[s_i + i][s_j + j]
            if tmp > answer:
                answer = tmp
            tmp = 0
    

for i in range(5):
    tetmino = tetmino_dic[i]

    if i == 0:
        conv(tetmino)
        conv(rotate90(tetmino))
        
    elif i == 1:
        conv(tetmino)

    elif i == 2 :
        
        for _ in range(4):
            tetmino = rotate90(tetmino)
            conv(tetmino)
        
        tetmino = symmetry(tetmino)
        for _ in range(4):
            tetmino = rotate90(tetmino)
            conv(tetmino)

    elif i == 3:
        conv(tetmino)
        conv(rotate90(tetmino))
        tetmino = symmetry(tetmino)
        conv(tetmino)
        conv(rotate90(tetmino))

    elif i == 4:
        for _ in range(4):
            tetmino = rotate90(tetmino)
            conv(tetmino)

print(answer)
