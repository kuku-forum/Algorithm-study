'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.21ms, 10.3MB)
테스트 5 〉	통과 (0.79ms, 10.3MB)
테스트 6 〉	통과 (2.92ms, 10.3MB)
테스트 7 〉	통과 (15.79ms, 10.3MB)
테스트 8 〉	통과 (58.91ms, 10.3MB)
테스트 9 〉	통과 (319.53ms, 10.3MB)
테스트 10 〉	통과 (1597.52ms, 10.3MB)
테스트 11 〉	통과 (9217.37ms, 10.3MB)
'''
answer = 0

def back(queen, row, col_lst, board):
    global answer
    dirc_lst = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    
    for j in range(len(board[0])):
        queen_break = False
        if col_lst[j] == 1:
            continue
            
        board[row][j] = 1
        
        
        for dirc in dirc_lst:
            ni = row
            nj = j

            while True:
                ni += dirc[0]
                nj += dirc[1]

                if len(board) > ni >= 0 and len(board) > nj >= 0:
                    if board[ni][nj] == 1:
                        queen_break = True
                        break
                else:
                    break

            if queen_break:
                board[row][j] = 0
                col_lst[j] = 0
                break

        if not queen_break:
            if queen == 1:
                answer += 1
                board[row][j] = 0
                col_lst[j] = 0
                return
            else:
                col_lst[j] = 1
                back(queen-1, row+1, col_lst, board)
                board[row][j] = 0
                col_lst[j] = 0

def solution(n):
    board_lst = [[0 for _ in range(n)] for _ in range(n)]
    col_lst = [0 for _ in range(n)]
    row = 0
    back(n, row, col_lst, board_lst)
    return answer