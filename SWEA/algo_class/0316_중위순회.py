from my_package.hjtc import swea_tc as print

def in_order(n):
    if n == 0:
        return
    in_order(left[n])
    answer.append(n)
    visited[n] = 1
    
    in_order(right[n])
    if visited[n] == 0:
        answer.append(n)

for t in range(1, 11):
    N = int(input())
    alp_dic = {}
    left = [0 for _ in range(N + 1)]
    right = [0 for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    answer = []
    
    for _ in range(N):
        info = list(input().split())
        if len(info) == 2:
            alp_dic[int(info[0])] = info[1]
        elif len(info) == 3:
            alp_dic[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
        elif len(info) == 4:
            alp_dic[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
            
    in_order(1)
    
    print(f"#{t} {''.join([alp_dic[i] for i in answer])}")