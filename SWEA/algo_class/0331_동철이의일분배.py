from my_package.hjtc import swea_tc # as print

def dfs1(r, total_percent):
    global max_percent, cnt
    cnt += 1
    # 1번 가지치기: 재귀를 통해 total_percent가 0 일경우
    if total_percent == 0:
        return
    
    if max_percent > total_percent:
        return
    
    if r == N:
        # max_percent = max(max_percent, total_percent)
        max_percent = total_percent
        return
    
    for c in range(N):
        # 2번 가지치기: for를 통해 board[r][c]가 0 일경우
        if board[r][c] == 0:
            continue
        
        if c_visited[c] == 0:
            c_visited[c] = 1
            dfs1(r+1, total_percent*board[r][c])
            c_visited[c] = 0
            
            
def dfs2(r, total_percent):
    global max_percent, cnt
    cnt += 1
    # # 1번 가지치기: 재귀를 통해 total_percent가 0 일경우
    # if total_percent == 0:
    #     return
    
    if max_percent > total_percent:
        return
    
    if r == N:
        # max_percent = max(max_percent, total_percent)
        max_percent = total_percent
        return
    
    for c in range(N):
        # 2번 가지치기: for를 통해 board[r][c]가 0 일경우
        if board[r][c] == 0:
            continue
        
        if c_visited[c] == 0:
            c_visited[c] = 1
            dfs2(r+1, total_percent*board[r][c])
            c_visited[c] = 0
            
            
def convert(x):
    return int(x)*0.01

cnt_lst1 = []
cnt_lst2 = []

for t in range(1, int(input())+1):
    max_percent = 0
    cnt = 0
    N = int(input())
    board = [list(map(convert, input().split())) for _ in range(N)]
    c_visited = [0 for _ in range(N)]
    
    dfs1(0, 1)
    print(f'#{t} {max_percent*100:0.6f}', cnt)
    cnt_lst1.append(cnt)
    
print(cnt_lst1)
# for t in range(1, int(input())+1):
#     max_percent = 0
#     cnt = 0
#     N = int(input())
#     board = [list(map(convert, input().split())) for _ in range(N)]
#     c_visited = [0 for _ in range(N)]
    
#     dfs2(0, 1)
#     print(f'#{t} {max_percent*100:0.6f}', cnt)
#     cnt_lst2.append(cnt)
    


'''
print(cnt_lst1)
1번 가지치기, 재귀를 더 많이 함
[21, 1361724, 2, 2973, 8142, 65, 19179765, 1392993, 1777865, 4, 17981, 220, 
2, 13, 6388, 718, 33, 20677, 651, 8790, 11550, 90, 595, 69559, 4991454, 307806, 
23999, 3484639, 65, 2850187, 5, 14, 2406, 8700, 121, 30603267, 34, 253, 62955,
21084, 50, 5, 10, 926, 54, 5, 73, 444718, 1084, 5733, 1368885, 127, 2984021,
11, 1647, 7685158, 41245, 13, 1339, 5041490, 578, 413218, 15, 163936, 2785, 
2534508, 5, 905651, 68579, 1888404, 2462, 905693, 2316, 37, 10285, 4375, 4121, 
5208, 37, 107, 7335, 782827, 265, 5799, 243, 5, 1708, 17728, 2700668, 50447,
13327, 21114, 14, 1119485, 998, 34, 59, 5418824, 216934, 29]  

print(cnt_lst2)
2번 가지치기
[21, 1356599, 2, 2973, 8142, 65, 17128006, 1371364, 1748486, 4, 17981, 214, 
2, 13, 6388, 718, 33, 20091, 651, 8760, 11550, 89, 595, 69559, 4987605, 307085, 
23013, 3413573, 65, 2850104, 5, 14, 2392, 8622, 118, 30603164, 34, 253, 62886,
21084, 50, 5, 10, 920, 54, 5, 73, 433917, 1084, 5563, 1291625, 127, 2903583,
11, 1647, 7520989, 38171, 13, 1329, 5015857, 559, 412984, 15, 163936, 2785, 
2528252, 5, 894249, 67987, 1884888, 2363, 897695, 2316, 37, 10285, 4375, 4077, 
5207, 37, 107, 7330, 759760, 261, 5799, 243, 5, 1624, 17042, 2660501, 50447,
13327, 21114, 12, 1119473, 998, 30, 59, 5261919, 216913, 26]  
'''