import sys

'''
slect = (i,j)
horizontal: i, range(N)
vertical : range(N), j
diagonal_u : i-min(i, j), j-min(i, j) ~ i+N-max(i, j)-1, j+N-max(i, j)-1
diagonal_d : i-min(i, j), j-min(i, j) ~ i+N-max(i, j)-1, j+N-max(i, j)-1

'''
N = int(sys.stdin.readline())
answer = 0
Q_map = [[True for _ in range(N)] for _ in range(N)]

def queen():

