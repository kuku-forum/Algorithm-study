import sys

N = int(sys.stdin.readline())
board_list = []

for _ in range(N):
    board_list.append(list(sys.stdin.readline().rstrip()))

search = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(graph):

    cnt_list, visited, stack = [], [], []

    for i in range(N):
        for j in range(N):
            if int(graph[i][j])and (i, j) not in visited:
                stack.append((i, j))
                cnt = 0

                while stack:
                    node = stack.pop()

                    if int(graph[node[0]][node[1]]) and node not in visited:
                        visited.append(node)
                        graph[node[0]][node[1]] = str(cnt)

                        for move in search:
                            tmp_i = node[0] + move[0]
                            tmp_j = node[1] + move[1]
                            
                            if tmp_i >= 0 and tmp_j >= 0 and N > tmp_i and N > tmp_j:
                                stack.append((tmp_i, tmp_j))
                        cnt += 1
                cnt_list.append(cnt)
    return cnt_list

answer = dfs(board_list)
answer.sort()

print(len(answer))
print(*answer, sep = '\n')

# for i in answer:
#     print(i)



# def dfs(graph):
#     visited = []
#     stack = []
#     cnt = 1

#     for i in range(N):
#         for j in range(N):
#             if int(graph[i][j])and (i, j) not in visited:
#                 # print(i, j, visited)
#                 stack.append((i, j))

#                 while stack:
#                     node = stack.pop()
#                     # print(node, stack, visited)

#                     if int(graph[node[0]][node[1]]) and node not in visited:
#                         visited.append(node)
#                         # print(type(int(graph[node[0]][node[1]])), visited)
#                         graph[node[0]][node[1]] = str(cnt)

#                         for move in search:
#                             tmp_i = node[0] + move[0]
#                             tmp_j = node[1] + move[1]
#                             if tmp_i >= 0 and tmp_j >= 0 and N > tmp_i and N > tmp_j:
#                                 stack.append((tmp_i, tmp_j))
#                 cnt += 1
#     return graph

# board = dfs(board_list)
