from my_package.hjtc import swea_tc as print
from pprint import pprint



def solution(board):
    
    word = ['' for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            
            for n in range(M//2):
                word[j + M//2] = board[i][j + M//2]
                word[j + n] = board[i][j + n]
                word[M + j - n - 1] = board[i][M + j - n - 1]
                
                if j + n > M + j - n - 1:
                    word = ['' for _ in range(N)]
                    break
                if board[i][j + n] != board[i][M + j - n - 1]:
                    word = ['' for _ in range(N)]
                    break
            else:
                return word
            
            
                
    for i in range(N - M + 1):
        for j in range(N):
            
            for n in range(M//2):
                word[i + M//2] = board[i + M//2][j]
                word[i + n] = board[i + n][j]
                word[M + i - n - 1] = board[M + i - n - 1][j]
                
                if i + n > M + i - n - 1:
                    word = ['' for _ in range(N)]
                    break
                
                if board[i + n][j] != board[M + i - n - 1][j]:
                    word = ['' for _ in range(N)]
                    break
            else:
                return word
    return



for t in range(1, int(input()) + 1):
    
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input())
    
    answer = solution(board)
    print(f'#{t} {"".join(answer).strip()}')
    