# import sys
# from itertools import permutations

# T = list(map(int,sys.stdin.readline().split()))
# N, M  = T[0], T[1]

# N_list = [i for i in range(1, N+1)]
# N_per = list(permutations(N_list, M))

# for num in N_per:
#     print(*num, sep=' ')


n,m = list(map(int,input().split())) #4 4
s = []
cnt = 1
 
def dfs():
    if len(s)==m: # 4
        global cnt
        # print(' '.join(map(str,s)))
        cnt += 1
        return
    
    for i in range(1,n+1): # 1,2,3,4
        if i not in s:
            s.append(i)
            print(cnt, i, s)
            dfs()
            s.pop()
 
dfs()