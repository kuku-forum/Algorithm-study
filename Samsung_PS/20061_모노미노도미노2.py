'''
95/153

조건
> 좌표 (x, y)에서 x는 행, y는 열을 의미한다
> (t, x, y)
> 블록: 1×1, 1×2, 2×1 
> t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
> t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
> t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우

> 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동
> 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다
> 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동
> 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한
> 연한색으로 표현되어 있는 특별한 칸, 아래 행에 있는 타일이 사라지고, 행의 수만큼 아래로 이동
> 행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다
> 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 연한 칸에 블록이 있는 경우를 처리

구현
0. 초록색 board, 파란색 board 따로 제작
1. 초록색블록과 파란색블록(transpose) 제작
2. board의 위에서 부터 검사하여 가장 행이 높은 빈공간을 찾음 및 배치
3. 배치가 끝난 후에 맨 아래서부터 all()함수를 통해 삭제될 행을 찾음
3_1. 삭제될 행이 있으면, 위에서부터 한칸씩 가져옴 모든 행이 all()이 아닐경우 3번 break
4. 연한칸 2번 행을 any()를 통해 확인 반복
4_1. 아래로 한칸식 떨어트림
'''
    
N = int(input())
command = []

for _ in range(N):
    command.append(list(map(int, input().split())))

# 파란색 보드도 초록색 보드와 똑같이 제작
green_board = [[0 for _ in range(4)] for _ in range(6)]
blue_board = [[0 for _ in range(4)] for _ in range(6)]

answer = 0


# t에 따라 초록색 블록 생성
def green_block_make(t, x, y):
    if t == 1:
        return [[x, y]]
    elif t == 2:
        return [[x, y], [x, y + 1]]
    elif t == 3:
        return [[x, y], [x + 1, y]]
    
    
# 초록색 블록의 x, y위치를 바꿔 파란색 블록 생성
def blue_block_make(block):
    result = []
    
    for nx, ny in block:
        result.append([ny, nx])
        
    return result


# 블록 배치
def block_drop(board, block):
    # 배치할 행의 위치인 select_y 선언
    select_y = ''
    flag = False
    
    # 높은 행에서 부터 배치된 블록이 있는지 확인
    for i in range(6):
        # 행(i)의 열(x)에 블록이 있을경우 한칸 위 행을 select_y로 선정
        for _, x in block:
            if board[i][x] == 1:
                select_y = i - 1
                flag = True
                break
        if flag:
            break
    # board의 행에 배치된 블록이 없다면 최대 행에 블록을 둬야함
    else:
        select_y = 5
    
    # 블록의 모양이 1x1이거나 가로가 긴 것일 경우 아래 진행 
    if len(block) == 1 or block[0][0] == block[1][0]:
        for _, x in block:
            board[select_y][x] = 1
    # 블록의 모양이 길쭉하다면, select_y의 값을 조절해서 설정
    else:
        for _, x in block:
            board[select_y][x] = 1
            select_y -= 1


# 한 행씩 검사
def bingo(board):
    cnt = 0
    # 더이상 검사 될게 없다면 종료
    while True:
        flag = True
        
        # 보드의 5번째(최대)행에서 2번째행 까지 all() 함수를 통해 검사
        for i in range(5, 1, -1):
            if all(board[i]):
                flag = False
                # 만약 한 행이 전부 1이라면 제거를 위한 중력 작용
                gravity(i, board)
                cnt += 1
        if flag:
            break
    return cnt


# 행 제거 및 아래를 당기기
def gravity(idx, board):
    # 제거가 필요한 행부터 첫번째 행까지 진행
    for i in range(idx, -1, -1):
        # 아래행에 위의 행의 값을 넣음
        if i - 1 >= 0:
            board[i] = board[i - 1]
        # 맨 위의 행에 도달하면 빈칸의 행을 넣음
        else:
            board[i] = [0, 0, 0, 0]


# 연한 칸에 블록이 있는지 확인
def light_color_chk(board):
        
    while True:
        flag = True
        # any()를 통해 1번 행에 숫자가 있다면 중력 작용, 총 두번 검사
        if any(board[1]):
            # 중력은 모든 칸에 적용되므로 5번째(마지막)행부터 적용
            gravity(5, board)
            flag = False
            
        if flag:
            break


# count함수를 통해 1의 개수 확인
def block_cnt(board):
    result = 0
    for i in range(2, 6, 1):
        result += board[i].count(1)
    return result


# 블록 제작 > 보드에 배치 > 빙고 검사 > 연한 부위 검사, 반복
for t, x, y in command:
    green_block = green_block_make(t, x, y)
    blue_block = blue_block_make(green_block)
    
    block_drop(green_board, green_block)
    block_drop(blue_board, blue_block)
    
    answer += bingo(green_board)
    answer += bingo(blue_board)
    
    light_color_chk(green_board)
    light_color_chk(blue_board)
    
block_num = block_cnt(green_board) + block_cnt(blue_board)
print(answer)
print(block_num)
