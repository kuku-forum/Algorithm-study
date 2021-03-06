'''
A 는 5로 이뤄짐

봄: 
나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

여름:
봄에 죽은 나무가 양분으로 변하게 된다
죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가(소수점 절삭)

가을:
번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 

겨울:
S2D2가 땅을 돌아다니면서 땅에 양분을 추가

K년 후 나무의 개수
나무의 위치 (x, y), 나이
'''


from collections import defaultdict, deque

direct_list = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
N, M, K = map(int, input().split())

A = []
food = [[5 for _ in range(N)] for _ in range(N)]
tree_board = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, input().split())))

tree_dic = defaultdict(deque)

# for _ in range(M):
#     x, y, z = map(int, input().split())
#     tree_dic[(x - 1, y - 1)].append(z)
    
# for x, y in tree_dic:
#     tree_board[x][y] = deque(sorted(tree_dic[(x, y)], reverse=True))
    
# def sping_summer():
#     for x in range(N):
#         for y in range(N):
#             tree_num = len(tree_board[x][y])
#             death_tree = 0
            
#             for _ in range(tree_num):
#                 age = tree_board[x][y].pop()
#                 if food[x][y] >= age:
#                     food[x][y] -= age
#                     tree_board[x][y].appendleft(age + 1)        
#                 else:
#                     death_tree += age//2
#             food[x][y] += death_tree

tree_board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree_board[x - 1][y - 1].append(z)
        

def sping_summer():
    # 나무 전체를 다 탐색
    for x in range(N):
        for y in range(N):
            aged = []
            death_tree = 0
            # 나무가 있으면 정렬해서 작은것부터 순회
            for age in sorted(tree_board[x][y]):
                # 양분 먹고 나이 올림, 양분 떨어지면 죽은 것으로 처리
                # aged라는 리스트 만들어서 한살 더 먹은 나무 리스트 삽입
                if food[x][y] >= age:
                    food[x][y] -= age
                    aged.append(age + 1)
                else:
                    death_tree += age//2
                    
            # 죽어서 만들어진 양분 업데이트
            # 기존 board에 변경
            food[x][y] += death_tree
            tree_board[x][y] = aged
        


def fall_winter():
    # board 전체 다 탐색해서, 5로 나눠질 경우 주변에 1살 나무 추가
    for x in range(N):
        for y in range(N):
            for age in tree_board[x][y]:
                if age%5 == 0:
                    
                    for dx, dy in direct_list:
                        nx = x + dx
                        ny = y + dy
                        
                        if N > nx >= 0 and N > ny >= 0:
                            tree_board[nx][ny].append(1)
            
            # 모든 board를 돌때 A에 있는 양분 추가
            food[x][y] += A[x][y]
                        
            

for k in range(K):
    sping_summer()
    fall_winter()

answer = 0

for x in range(N):
    for y in range(N):
        answer += len(tree_board[x][y])
    
print(answer)



tree_dic = defaultdict(deque)

for _ in range(M):
    x, y, z = map(int, input().split())
    # tree[x - 1][y - 1].append(z)
    tree_dic[(x - 1, y - 1)].append(z)
    
direct_list = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for x, y in tree_dic:
    tree_dic[(x, y)] = deque(sorted(tree_dic[(x, y)], reverse=True))
    
# dictionary -> que -> list
def sping_summer():
    tree_keys = list(tree_dic.keys())
    # for x, y in tree_keys:
    print(tree_dic.keys())
    for x, y in tree_dic.keys():
        print(x, y)
        # tree_dic[(x, y)] = deque(sorted(tree_dic[(x, y)], reverse=True))
        # print(tree_dic)
        tree_num = len(tree_dic[(x, y)])
        death_tree = 0
        que = deque([])
        for _ in range(tree_num):
            age = tree_dic[(x, y)].pop()
            
            if food[x][y] >= age:
                food[x][y] -= age
                # tree_dic[(x, y)].appendleft(age + 1)
                que.appendleft(age + 1)        
            else:
                death_tree += age//2
        
        tree_dic[(x, y)] = que
        if not tree_dic[(x, y)]:
            del tree_dic[(x, y)]
            
        food[x][y] += death_tree

def fall():
    tree_keys = list(tree_dic.keys())
    for x, y in tree_keys:
    # for x, y in tree_dic.keys():
        for age in tree_dic[(x, y)]:
            if age%5 == 0:
                for dx, dy in direct_list:
                    nx = x + dx
                    ny = y + dy
                    
                    if N > nx >= 0 and N > ny >= 0:
                        tree_dic[(nx, ny)].append(1)
                        
def winter():
    for x in range(N):
        for y in range(N):
            food[x][y] += A[x][y]
            

for _ in range(K):
    sping_summer()
    fall()
    winter()

answer = 0
for x, y in tree_dic:
    answer += len(tree_dic[(x, y)])
    
print(answer)



for i in dict.keys():
    print(dict[i])
    dict[3] = 4
    
