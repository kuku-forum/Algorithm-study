import sys

N = int(sys.stdin.readline())
mat_fibo = [[1, 1],[1, 0]]
sub = 1000000007

def mul_mat(mat1, mat2):
    mat_tmp = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            tmp = 0
            for k in range(len(mat2)):
                tmp += mat1[i][k]*mat2[k][j]
            row.append(tmp%sub)
        mat_tmp.append(row)
    return mat_tmp


def pow_mat(mat_base, exp):
    
    if exp==1:
        for i in range(len(mat_base)):
            for j in range(len(mat_base[0])):
                mat_base[i][j] = mat_base[i][j]%sub
        return mat_base

    elif exp%2 == 0:
        mat_val = pow_mat(mat_base, exp//2)
        return mul_mat(mat_val, mat_val)

    else:
        mat_val = pow_mat(mat_base, exp-1)
        return mul_mat(mat_val, mat_base)


mat_result = pow_mat(mat_fibo, N)
print(mat_result[0][1])
