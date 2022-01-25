N = int(input())
board = list(map(int, input().split()))

T = int(input())
com_list = []

for _ in range(T):
    com_list.append(list(map(int, input().split())))


def switch(val):
    if val == 1: return 0
    return 1

def female(n):
    chk_list = [n - 1]
    fowd = n
    back = n - 2
    
    while True:
        
        if N > fowd >= 0 and N > back >= 0:
            if board[fowd] == board[back]:
                chk_list.append(fowd)
                chk_list.append(back)
            else:
                break
        else:
            break
    
        fowd += 1
        back -= 1
        
    for chk in chk_list:
        board[chk] = switch(board[chk])
    

def male(n):
    for i in range(1, N+1):
        mul_n = n*i
        if mul_n > N: break
        board[mul_n - 1] = switch(board[mul_n - 1])
        

for gender, idx in com_list:
    
    if gender == 1:
        male(idx)
    else:
        female(idx)


flag = False
for start in range(0, N, 20):
    row = []
    for j in range(start, start + 20):
        if j >= N:
            flag = True
            break
        row.append(board[j])
    print(' '.join(map(str, row)))
        
    if flag:
        break