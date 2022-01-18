
'''
0-w, 0-w
0-w, w-2w
w-2w, 0-w
w-2w, w-2w
'''
import sys

N = int(sys.stdin.readline())
paper_T = []

for _ in range(N):
    paper_T.append(list(map(int, sys.stdin.readline().split())))

blue_num = 0
white_num = 0

def div_conq(paper, window):
    global blue_num, white_num

    if window == N//2:
        sum_val = 0
        for row in paper:
            sum_val += sum(row)
        if sum_val == N**2:
            blue_num += 1
            return
        elif sum_val == 0:
            white_num += 1
            return

    idx_list = [(0, window, 0, window), (0, window, window, window*2), 
    (window, window*2, 0, window), (window, window*2, window, window*2)]

    for idx in idx_list:
        tmp_paper = [] 
        sum_val = 0

        for i in range(idx[0], idx[1]):
            tmp_row = []
            for j in range(idx[2], idx[3]):
                tmp_row.append(paper[i][j])
            tmp_paper.append(tmp_row)
        
        for i in tmp_paper:
            sum_val += sum(i)
        
        if sum_val == window**2:
            blue_num +=1
        elif sum_val == 0:
            white_num += 1
        else:
            div_conq(tmp_paper, window//2)

    return

div_conq(paper_T, N//2)
print(white_num)
print(blue_num)