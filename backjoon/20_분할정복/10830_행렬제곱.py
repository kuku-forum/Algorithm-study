import sys

N,B = map(int, sys.stdin.readline().split())
mat_A = []

for _ in range(N):
    mat_A.append(list(map(int, sys.stdin.readline().split())))

cnt = 1
def pow_mat(mat_base, exp):
    global cnt
    print(cnt, exp)
    cnt +=1

    if exp==1:
        for i in range(N):
            for j in range(N):
                mat_base[i][j] %= 1000
        return mat_base
    
    elif exp % 2 == 0:
        mat_val = pow_mat(mat_base, exp//2)
        mat_tmp = []
        for y in range(N):
            row = []
            for x in range(N):
                tmp = 0
                for i in range(N):
                    tmp += mat_val[y][i] * mat_val[i][x]
                row.append(tmp%1000)
            mat_tmp.append(row)
        return mat_tmp
    
    else:
        mat_val = pow_mat(mat_base, exp-1)
        mat_tmp = []

        for y in range(N):
            row = []
            for x in range(N):
                tmp = 0
                for i in range(N):
                    tmp += mat_val[y][i] * mat_base[i][x]
                row.append(tmp%1000)
            mat_tmp.append(row)
        return mat_tmp

mat_result = pow_mat(mat_A, B)

for i in range(N):
    for j in range(N):
        print(mat_result[i][j], end = ' ')
    print()
