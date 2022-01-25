w, h = map(int, input().split())
N = int(input())
cut_list = []

for _ in range(N):
    cut_list.append(list(map(int, input().split())))

row_list = [0, w]
col_list = [0, h]

for direct, cut in cut_list:
    if direct == 0:
        col_list.append(cut)
    else:
        row_list.append(cut)

col_list.sort()
row_list.sort()

col_cut_list = []
row_cut_list = []

for i in range(1, len(col_list)):
    col_cut_list.append(col_list[i] - col_list[i-1])
    
for i in range(1, len(row_list)):
    row_cut_list.append(row_list[i] - row_list[i-1])

col_cut_list.sort()
row_cut_list.sort()

print(col_cut_list[-1]*row_cut_list[-1])
