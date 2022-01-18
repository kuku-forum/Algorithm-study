N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# 서, 북, 동, 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
distance = []

for i in range(1, N):
    distance.append(i)
    distance.append(i)
distance.append(N-1)

pos = [[N//2, N//2]]

splash_W = {(-1, 0): 0.07, (1, 0): 0.07, (-1, 1): 0.01, (1, 1): 0.01,
            (-2, 0): 0.02, (2, 0): 0.02, (-1, -1): 0.1, (1, -1): 0.1, (0, -2): 0.05}

splash_S = {(0, 1): 0.07, (0, -1): 0.07, (-1, 1): 0.01, (-1, -1): 0.01,
            (0, 2): 0.02, (0, -2): 0.02, (1, -1): 0.1, (1, 1): 0.1, (2, 0): 0.05}

splash_E = {(-1, 0): 0.07, (1, 0): 0.07, (-1, -1): 0.01, (1, -1): 0.01,
            (-2, 0): 0.02, (2, 0): 0.02, (-1, 1): 0.1, (1, 1): 0.1, (0, 2): 0.05}

splash_N = {(0, -1): 0.07, (0, 1): 0.07, (1, -1): 0.01, (1, 1): 0.01,
            (0, -2): 0.02, (0, 2): 0.02, (-1, -1): 0.1, (-1, 1): 0.1, (-2, 0): 0.05}


splash_lst = [splash_W, splash_S, splash_E, splash_N]
direct_damage = [(0, -1), (1, 0), (0, 1), (1, 0)]

cnt = 1
answer = 0
print(distance)
for i, dist in enumerate(distance):
    for _ in range(1, dist+1):


        # print('#1',i, pos[-1][0], pos[-1][0])
        # print('#2', [i % (N-1)], [i % (N-1)])
        y = dy[i % 4] + pos[-1][0]
        x = dx[i % 4] + pos[-1][1]
        # print(pos)
        pos.append([y, x]) # 현재 위치

        print()
        print(i, answer, y, x, pos[-2][0], pos[-2][1], dy[i % 4], dx[i % 4])

        if board[y][x] > 9:
            # 현재위치에 있는 모래
            sand = board[y][x]
            for point in splash_lst[i % 4]:
                # splash 위치 파악
                ny = y + point[0]
                nx = x + point[1]
                damage = int(splash_lst[i % 4][(point[0], point[1])] * board[y][x])
                print(splash_lst[i % 4][(point[0], point[1])],board[y][x], damage)

                if N > ny >= 0 and N > nx >= 0 and damage > 0:
                    board[ny][nx] += damage
                    sand -= damage
                else:
                    answer += damage
                    sand -= damage
            else:
                ny = y + direct_damage[i % 4][0]
                nx = x + direct_damage[i % 4][1]
                print('#2', i, y, x, ny, nx, sand)

                if N > ny >= 0 and N > nx >= 0:
                    board[ny][nx] += sand
                    board[y][x] = 0
                else:
                    answer += sand
                    board[y][x] = 0

        elif 9 >= board[y][x] > 0:
            sand = board[y][x]
            ny = y + direct_damage[i % 4][0]
            nx = x + direct_damage[i % 4][1]

            if N > ny >= 0 and N > nx >= 0:
                print('#3', ny, nx, y, x)
                board[ny][nx] += sand
                board[y][x] = 0
            else:
                answer += sand
                board[y][x] = 0
        else:
            continue

        for row in board:
            print(row)

print(answer)
print(board)










