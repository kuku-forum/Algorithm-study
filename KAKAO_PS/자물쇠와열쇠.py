
'''
정확성  테스트
테스트 1 〉	통과 (0.33ms, 10.4MB)
테스트 2 〉	통과 (0.16ms, 10.3MB)
테스트 3 〉	통과 (2.95ms, 10.3MB)
테스트 4 〉	통과 (0.09ms, 10.5MB)
테스트 5 〉	통과 (4.52ms, 10.3MB)
테스트 6 〉	통과 (2.70ms, 10.3MB)
테스트 7 〉	통과 (2.87ms, 10.4MB)
테스트 8 〉	통과 (24.44ms, 10.4MB)
테스트 9 〉	통과 (16.34ms, 10.3MB)
테스트 10 〉	통과 (59.76ms, 10.3MB)
테스트 11 〉	통과 (42.54ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.4MB)
테스트 13 〉	통과 (1.89ms, 10.4MB)
테스트 14 〉	통과 (0.86ms, 10.3MB)
테스트 15 〉	통과 (1.29ms, 10.3MB)
테스트 16 〉	통과 (11.66ms, 10.3MB)
테스트 17 〉	통과 (1.12ms, 10.3MB)
테스트 18 〉	통과 (3.03ms, 10.3MB)
테스트 19 〉	통과 (0.24ms, 10.3MB)
테스트 20 〉	통과 (13.06ms, 10.3MB)
테스트 21 〉	통과 (4.62ms, 10.4MB)
테스트 22 〉	통과 (6.13ms, 10.3MB)
테스트 23 〉	통과 (1.12ms, 10.3MB)
테스트 24 〉	통과 (1.54ms, 10.3MB)
테스트 25 〉	통과 (13.62ms, 10.3MB)
테스트 26 〉	통과 (35.08ms, 10.3MB)
테스트 27 〉	통과 (59.81ms, 10.3MB)
테스트 28 〉	통과 (4.50ms, 10.3MB)
테스트 29 〉	통과 (1.90ms, 10.3MB)
테스트 30 〉	통과 (6.97ms, 10.3MB)
테스트 31 〉	통과 (7.49ms, 10.3MB)
테스트 32 〉	통과 (23.58ms, 10.3MB)
테스트 33 〉	통과 (7.62ms, 10.3MB)
테스트 34 〉	통과 (0.29ms, 10.4MB)
테스트 35 〉	통과 (0.97ms, 10.3MB)
테스트 36 〉	통과 (1.29ms, 10.3MB)
테스트 37 〉	통과 (0.90ms, 10.2MB)
테스트 38 〉	통과 (0.19ms, 10.3MB)
'''
from pprint import pprint

def rot90(arr):
    return list(map(list, zip(*reversed(arr))))


def pad_board(pad, lock):
    length = 2*(pad-1) + len(lock)
    board = [[2 for _ in range(length)] for _ in range(length)]
    
    for ly, by in enumerate(range(pad-1, len(lock) + pad-1)):
        for lx, bx in enumerate(range(pad-1, len(lock) + pad-1)):
            board[by][bx] = lock[ly][lx]
            
    return board


def check(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            
            if board[i][j] == 0:
                return False
    return True
    
    
def conv(key, lock):
    
    for y in range(len(lock) - len(key) + 1):
        for x in range(len(lock) - len(key) + 1):
            break_trigger = False
            key_pos = []
            
            for ky in range(len(key)):
                for kx in range(len(key)):
                    ly = y + ky
                    lx = x + kx
                    
                    if lock[ly][lx] == 2:
                        continue
                    
                    if lock[ly][lx] == 0 and key[ky][kx] == 1:
                        key_pos.append([ly, lx])
                    elif lock[ly][lx] == 1 and key[ky][kx] == 0:
                        continue
                    else:
                        break_trigger = True
                        break
                        
                if break_trigger:
                    break
            
            if not break_trigger:
                
                ## y, x로 하면 안됨 이유는 모르겠음
                for py, px in key_pos:
                    lock[py][px] = 1
                if check(lock):
                    return True
                for py, px in key_pos:
                    lock[py][px] = 0
                    
                # for y, x in key_pos:
                #     lock[y][x] = 1
                # if check(lock):
                #     return True
                # for y, x in key_pos:
                #     lock[y][x] = 0
    return False


def solution(key, lock):
    
    lock = pad_board(len(key), lock)
    
    # pprint(lock)
    
    for _ in range(4):
        key = rot90(key)
        if conv(key, lock):
            return True
        
    return False