

# def white_cnt(board, K):
#     cnt = 0
#     for row in board:
#         row = ''.join(row)
        
#         for part in row.split('0'):
#             if len(part) == K:
#                 cnt += 1
#     return cnt


# def solution(board, K):
#     result = 0
#     result += white_cnt(board, K)
#     board = rot90(board)
#     result += white_cnt(board, K)
#     return result


# T = int(input())

# for t in range(1, T + 1):
#     board = []
#     N, K = map(int, input().split())
#     for _ in range(N):
#         board.append(input().split())
#     answer = solution(board, K)
#     print(f'#{t} {answer}')



def rot90(arr):
    return list(map(list, zip(*reversed(arr))))

def word_chk(i, j):
    for k in range(j, j + K):
        if k >= N:
            return 0
        
        if board[i][k] == 0 :
            return 0
        
    if (j-1 == -1 or board[i][j - 1] == 0) and (k + 1 == N or board[i][k + 1] == 0):
        print(i, j, k)
        return 1
                        
    return 0 



T = int(input())

for t in range(1, T + 1):
    board = []
    N, K = map(int, input().split())
    for _ in range(N):
        board.append(list(map(int, input().split())))
        
    answer = 0
    
    for i in range(N):
        for j in range(N):
            
            if board[i][j] == 1:
                answer += word_chk(i, j)
                
    board = rot90(board)
    for i in range(N):
        for j in range(N):
            
            if board[i][j] == 1:
                answer += word_chk(i, j)
                
                
    print(f'#{t} {answer}')