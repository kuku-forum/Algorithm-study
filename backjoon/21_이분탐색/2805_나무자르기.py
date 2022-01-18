import sys

N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree_list)

while start <= end:
    cut = (start+end)//2
    answer = 0

    for tree in tree_list:
        tmp = tree-cut
        if tmp < 0: 
            tmp=0
        answer += tmp

    # print(start, end, cut, answer)

    if answer >= M:
        start = cut+1
        
    elif answer < M:
        end = cut-1

print(end)