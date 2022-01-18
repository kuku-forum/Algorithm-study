import sys
from collections import defaultdict
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())

cctv_func = {1: [[(0, 1)], 
                [(0, -1)], 
                [(1, 0)], 
                [(-1, 0)]],
            
            2: [
                [(0, 1), (0, -1)], 
                [(1, 0), (-1, 0)]],
            
            3: [
                [(0, 1), (-1, 0)], 
                [(0, 1), (1, 0)], 
                [(0, -1), (-1, 0)], 
                [(0, -1), (1, 0)]],
            
            4: [
                [(0, -1), (-1, 0), (0, 1)], 
                [(-1, 0), (0, 1), (1, 0)], 
                [(0, 1), (1, 0), (0, -1)], 
                [(1, 0), (0, -1), (-1, 0)]],

            5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]]
}

cctv_loc = defaultdict(list)
cctv_lst = []
wall_loc = []
ans = 0

for i in range(N):
    for j, num in enumerate(map(int, sys.stdin.readline().split())):
        if num in range(1,6):
            cctv_loc[i, j] = num
            cctv_lst.append((i, j))
        elif num == 6:
            wall_loc.append((i,j))


def dfs(tmp1, num):
    global ans

    if num >= len(cctv_lst):
        ans = max(ans, len(tmp1))
        return ans
    
    tmp2 = deepcopy(tmp1)
    cctv = cctv_loc[cctv_lst[num]]

    for func in cctv_func[cctv]:
        for f in func:

            y = cctv_lst[num][0]
            x = cctv_lst[num][1]
            
            while True:
                y -= f[0]
                x -= f[1]

                if N > y >= 0 and M > x >= 0 and (y, x) not in wall_loc:
                    if (y, x) in cctv_loc or (y, x) in tmp2:
                        continue
                    else:
                        tmp2.add((y, x))
                else:
                    break

        dfs(tmp2, num + 1)
        tmp2 = deepcopy(tmp1)

result = set()
dfs(result, 0)
print(N*M  - ans - len(cctv_loc) - len(wall_loc))