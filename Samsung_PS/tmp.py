import sys
from copy import deepcopy
sys.setrecursionlimit(100000000)

# 하, 좌, 우, 상
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def move(board, r, c, open_card, cnt, card_dict, test, visited):
    global answer
    print('#2', cnt, card_dict)
    # if cnt >= 20:
    #     return
    
    if cnt >= answer:
        return
    
    if open_card and (open_card[0], open_card[1]) == (r, c):
        return
    
    if not card_dict:
        print(test)
        answer = min(answer ,cnt)
        return
    
    
    # print('#3')
    if board[r][c] > 0:
        if not open_card:
            open_card = [r, c, board[r][c]]
        else:
            
            if open_card[-1] == board[r][c]:
                
                del card_dict[(open_card[0], open_card[1])]
                del card_dict[(r, c)]
                # print('#2', cnt, card_dict)
                # print(test)
                
                board[open_card[0]][open_card[1]] = 0
                board[r][c] = 0
                open_card = []
            else:
                open_card = [r, c, board[r][c]]
                cnt += 1
        cnt += 1
    
    for i, (dr, dc) in enumerate(directions):
        nr = r
        nc = c
        nr += dr
        nc += dc
        max_nr = 5
        max_nc = 5
        
        while 4 > nr >= 0 and 4 > nc >= 0:
            if board[nr][nc] > 0:
                max_nr = nr
                max_nc = nc
                # print(r, c, max_nr, max_nc)
                break
            nr += dr
            nc += dc
            
        else:
            max_nr = nr - dr
            max_nc = nc - dc
            
        # max case
        if max_nr == r and max_nc == c:
            continue
        else:
            # if open_card and (open_card[0], open_card[1]) != (max_nr, max_nc):
            if (r, c) != (max_nr, max_nc) and visited[max_nr][max_nc] == 0:
                # print(test)
                visited[max_nr][max_nc] = 1
                move(deepcopy(board), max_nr, max_nc, deepcopy(open_card), cnt + 1, deepcopy(card_dict), deepcopy(test + [(i, 'max')]), deepcopy(visited))
        
        # setep case
        nr = r
        nc = c
        step = 0
        for _ in range(4):
            nr += dr
            nc += dc
            step += 1
            
            if max_nr == nr and max_nc == nc:
                break
            else:
                # if open_card and (open_card[0], open_card[1]) != (nr, nc):
                if (r, c) != (nr, nc) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    move(deepcopy(board), nr, nc, deepcopy(open_card), cnt + step, deepcopy(card_dict), deepcopy(deepcopy(test + [(i)])), deepcopy(visited))
    return


def solution(board, r, c):
    print('start')
    global answer
    answer = 0xffff
    card_dict = {}
    
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                card_dict[(i, j)] = board[i][j]
                
    # print(card_dict)
    visited = [[0 for _ in range(4)] for _ in range(4)]
    visited[r][c] = 1
    
    move(deepcopy(board), r, c, [], 0, deepcopy(card_dict), deepcopy([]), deepcopy(visited))
    print(answer)
    return answer

solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
# solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)
