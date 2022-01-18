import sys

N = int(sys.stdin.readline())
q_list = [0 for _ in range(N)]
cnt = 0

def check(idx):
    for i in range(idx):
        if q_list[idx] == q_list[i] or idx-i == abs(q_list[idx] - q_list[i]):
            return False
    return True


def N_Queen(row):
    global cnt
    
    if row == N:
        cnt += 1
        return 1
    
    for column in range(N):
        q_list[row] = column

        if check(row):
            N_Queen(row+1)


N_Queen(0)
print(cnt)



# def solution(n: int):
#     return search([0] * n, 0)
 
 
# def search(queen: list, row: int):
#     n = len(queen)
#     count = 0
 
#     if n == row:
#         return 1
 
#     for col in range(n):
#         queen[row] = col
#         if check(queen, row):
#             count += search(queen, row + 1)
#     return count
 
 
# def check(queen: list, row: int):
#     for i in range(row):
#         if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
#             return False
 
#     return True

# print(solution(int(input())))