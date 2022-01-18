import sys

A, B, C = map(int, sys.stdin.readline().split())

def power(base, exponent):

    if exponent == 1:
        return base % C
    elif exponent%2 == 0:
        val = power(base, exponent//2)
        return (val**2)%C
    else:
        val = power(base, (exponent-1)//2)
        return (val**2*base)%C

print(power(A, B))