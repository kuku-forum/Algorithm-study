def rot90(arr):
    return list(map(list, zip(*reversed(arr))))


def white_cnt(board, K):
    cnt = 0
    for row in board:
        row = ''.join(row)
        
        for part in row.split('0'):
            if len(part) == K:
                cnt += 1
    return cnt


def solution(board, K):
    result = 0
    result += white_cnt(board, K)
    board = rot90(board)
    result += white_cnt(board, K)
    return result


T = int(input())

for t in range(1, T + 1):
    board = []
    N, K = map(int, input().split())
    for _ in range(N):
        # board.append(list(map(int, input().split())))
        board.append(input().split())
    print(board)
    answer = solution(board, K)
    print(f'#{t} {answer}')