## rotate2 : 해당 면을 돌릴 때 일어나는 면의 변화
def rotate2(array, direction):
    if direction == '-':    # 반시계방향
        array[0][0], array[0][2], array[2][2], array[2][0] = array[0][2], array[2][2], array[2][0], array[0][0]
        array[0][1], array[1][2], array[2][1], array[1][0] = array[1][2], array[2][1], array[1][0], array[0][1]
    elif direction == '+':  # 시계방향
        array[0][0], array[2][0], array[2][2], array[0][2] = array[2][0], array[2][2], array[0][2], array[0][0]
        array[0][1], array[1][0], array[2][1], array[1][2] = array[1][0], array[2][1], array[1][2], array[0][1]


## rotate : 해당 면을 돌릴 때, 주변에 일어나는 변화
def rotate(side, direction):
    if side == 'L':            # 왼쪽 면
        if direction == '-':   # 반시계방향
            dt['U'][0][0], dt['B'][-1][-1], dt['D'][0][0], dt['F'][0][0] = dt['F'][0][0], dt['U'][0][0], dt['B'][-1][-1], dt['D'][0][0]
            dt['U'][1][0], dt['B'][-2][-1], dt['D'][1][0], dt['F'][1][0] = dt['F'][1][0], dt['U'][1][0], dt['B'][-2][-1], dt['D'][1][0]
            dt['U'][2][0], dt['B'][-3][-1], dt['D'][2][0], dt['F'][2][0] = dt['F'][2][0], dt['U'][2][0], dt['B'][-3][-1], dt['D'][2][0]
        elif direction == '+': # 시계방향
            dt['U'][0][0], dt['F'][0][0], dt['D'][0][0], dt['B'][-1][-1] = dt['B'][-1][-1], dt['U'][0][0], dt['F'][0][0], dt['D'][0][0]
            dt['U'][1][0], dt['F'][1][0], dt['D'][1][0], dt['B'][-2][-1] = dt['B'][-2][-1], dt['U'][1][0], dt['F'][1][0], dt['D'][1][0]
            dt['U'][2][0], dt['F'][2][0], dt['D'][2][0], dt['B'][-3][-1] = dt['B'][-3][-1], dt['U'][2][0], dt['F'][2][0], dt['D'][2][0]
    elif side == 'R':          # 오른쪽 면
        if direction == '-':   # 반시계방향
            dt['U'][0][-1], dt['F'][0][-1], dt['D'][0][-1], dt['B'][-1][0] = dt['B'][-1][0], dt['U'][0][-1], dt['F'][0][-1], dt['D'][0][-1]
            dt['U'][1][-1], dt['F'][1][-1], dt['D'][1][-1], dt['B'][-2][0] = dt['B'][-2][0], dt['U'][1][-1], dt['F'][1][-1], dt['D'][1][-1]
            dt['U'][2][-1], dt['F'][2][-1], dt['D'][2][-1], dt['B'][-3][0] = dt['B'][-3][0], dt['U'][2][-1], dt['F'][2][-1], dt['D'][2][-1]
        elif direction == '+': # 시계방향
            dt['U'][0][-1], dt['B'][-1][0], dt['D'][0][-1], dt['F'][0][-1] = dt['F'][0][-1], dt['U'][0][-1], dt['B'][-1][0], dt['D'][0][-1]
            dt['U'][1][-1], dt['B'][-2][0], dt['D'][1][-1], dt['F'][1][-1] = dt['F'][1][-1], dt['U'][1][-1], dt['B'][-2][0], dt['D'][1][-1]
            dt['U'][2][-1], dt['B'][-3][0], dt['D'][2][-1], dt['F'][2][-1] = dt['F'][2][-1], dt['U'][2][-1], dt['B'][-3][0], dt['D'][2][-1]
    elif side == 'F':          # 앞면
        if direction == '-':   # 반시계방향
            dt['U'][-1][0], dt['L'][-1][-1], dt['D'][0][-1], dt['R'][0][0] = dt['R'][0][0], dt['U'][-1][0], dt['L'][-1][-1], dt['D'][0][-1]
            dt['U'][-1][1], dt['L'][-2][-1], dt['D'][0][-2], dt['R'][1][0] = dt['R'][1][0], dt['U'][-1][1], dt['L'][-2][-1], dt['D'][0][-2]
            dt['U'][-1][2], dt['L'][-3][-1], dt['D'][0][-3], dt['R'][2][0] = dt['R'][2][0], dt['U'][-1][2], dt['L'][-3][-1], dt['D'][0][-3]
        elif direction == '+': # 시계방향
            dt['U'][-1][0], dt['R'][0][0], dt['D'][0][-1], dt['L'][-1][-1] = dt['L'][-1][-1], dt['U'][-1][0], dt['R'][0][0], dt['D'][0][-1]
            dt['U'][-1][1], dt['R'][1][0], dt['D'][0][-2], dt['L'][-2][-1] = dt['L'][-2][-1], dt['U'][-1][1], dt['R'][1][0], dt['D'][0][-2]
            dt['U'][-1][2], dt['R'][2][0], dt['D'][0][-3], dt['L'][-3][-1] = dt['L'][-3][-1], dt['U'][-1][2], dt['R'][2][0], dt['D'][0][-3]
    elif side == 'B':          # 뒷면
        if direction == '-':   # 반시계방향
            dt['U'][0][-1], dt['R'][-1][-1], dt['D'][-1][0], dt['L'][0][0] = dt['L'][0][0], dt['U'][0][-1], dt['R'][-1][-1], dt['D'][-1][0]
            dt['U'][0][-2], dt['R'][-2][-1], dt['D'][-1][1], dt['L'][1][0] = dt['L'][1][0], dt['U'][0][-2], dt['R'][-2][-1], dt['D'][-1][1]
            dt['U'][0][-3], dt['R'][-3][-1], dt['D'][-1][2], dt['L'][2][0] = dt['L'][2][0], dt['U'][0][-3], dt['R'][-3][-1], dt['D'][-1][2]
        elif direction == '+': # 시계방향
            dt['U'][0][-1], dt['L'][0][0], dt['D'][-1][0], dt['R'][-1][-1] = dt['R'][-1][-1], dt['U'][0][-1], dt['L'][0][0], dt['D'][-1][0]
            dt['U'][0][-2], dt['L'][1][0], dt['D'][-1][1], dt['R'][-2][-1] = dt['R'][-2][-1], dt['U'][0][-2], dt['L'][1][0], dt['D'][-1][1]
            dt['U'][0][-3], dt['L'][2][0], dt['D'][-1][2], dt['R'][-3][-1] = dt['R'][-3][-1], dt['U'][0][-3], dt['L'][2][0], dt['D'][-1][2]
    elif side == 'U':          # 윗면
        if direction == '-':   # 반시계방향
            dt['F'][0][0], dt['R'][0][0], dt['B'][0][0], dt['L'][0][0] = dt['L'][0][0], dt['F'][0][0], dt['R'][0][0], dt['B'][0][0]
            dt['F'][0][1], dt['R'][0][1], dt['B'][0][1], dt['L'][0][1] = dt['L'][0][1], dt['F'][0][1], dt['R'][0][1], dt['B'][0][1]
            dt['F'][0][2], dt['R'][0][2], dt['B'][0][2], dt['L'][0][2] = dt['L'][0][2], dt['F'][0][2], dt['R'][0][2], dt['B'][0][2]
        elif direction == '+': # 시계방향
            dt['F'][0][0], dt['L'][0][0], dt['B'][0][0], dt['R'][0][0] = dt['R'][0][0], dt['F'][0][0], dt['L'][0][0], dt['B'][0][0]
            dt['F'][0][1], dt['L'][0][1], dt['B'][0][1], dt['R'][0][1] = dt['R'][0][1], dt['F'][0][1], dt['L'][0][1], dt['B'][0][1]
            dt['F'][0][2], dt['L'][0][2], dt['B'][0][2], dt['R'][0][2] = dt['R'][0][2], dt['F'][0][2], dt['L'][0][2], dt['B'][0][2]
    elif side == 'D':          # 아랫면
        if direction == '-':   # 반시계방향
            dt['F'][-1][0], dt['L'][-1][0], dt['B'][-1][0], dt['R'][-1][0] = dt['R'][-1][0], dt['F'][-1][0], dt['L'][-1][0], dt['B'][-1][0]
            dt['F'][-1][1], dt['L'][-1][1], dt['B'][-1][1], dt['R'][-1][1] = dt['R'][-1][1], dt['F'][-1][1], dt['L'][-1][1], dt['B'][-1][1]
            dt['F'][-1][2], dt['L'][-1][2], dt['B'][-1][2], dt['R'][-1][2] = dt['R'][-1][2], dt['F'][-1][2], dt['L'][-1][2], dt['B'][-1][2]
        elif direction == '+': # 시계방향
            dt['F'][-1][0], dt['R'][-1][0], dt['B'][-1][0], dt['L'][-1][0] = dt['L'][-1][0], dt['F'][-1][0], dt['R'][-1][0], dt['B'][-1][0]
            dt['F'][-1][1], dt['R'][-1][1], dt['B'][-1][1], dt['L'][-1][1] = dt['L'][-1][1], dt['F'][-1][1], dt['R'][-1][1], dt['B'][-1][1]
            dt['F'][-1][2], dt['R'][-1][2], dt['B'][-1][2], dt['L'][-1][2] = dt['L'][-1][2], dt['F'][-1][2], dt['R'][-1][2], dt['B'][-1][2]

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        M = int(input())
        dt = {
        'U' : [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']], #윗면
        'D' : [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], #아랫면
        'F' : [['r', 'r', 'r'], ['r', 'r', 'rS'], ['r', 'r', 'r']], #앞면
        'B' : [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], #뒷면
        'L' : [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']], #왼쪽면
        'R' : [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']], #오른쪽면
        }
        for x in input().split():
            side, direction = x[0], x[1]
            rotate(side, direction)          # 옆 면 회전
            rotate2(dt[side], direction)     # 해당 면 회전
        for i in dt['U']:
            print(''.join(i))


