from collections import defaultdict

T = int(input())

def solution():
    board = [[0 for _ in range(10)] for _ in range(10)]
    result = 0
    
    for y1, x1, y2, x2 in color_dic[1]:
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                board[y][x] = 1
                
    for y1, x1, y2, x2 in color_dic[2]:
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if board[y][x] == 1:
                    board[y][x] = 3
                    result += 1
    return result


for t in range(1, T + 1):
    N = int(input())
    color_dic = defaultdict(list)
    
    for _ in range(N):
        info = list(map(int, input().split()))
        color_dic[info[-1]].append(info[:-1])
          
    answer = solution()
    print(f'#{t} {answer}')