import sys

def w(a, b, c):
    
    if a<=0 or b<=0 or c<=0:
        return 1
        
    elif a>20 or b>20 or c>20:
        if (a, b, c) in dic_N:
            return dic_N[a, b, c]
        else:
            dic_N[a, b, c] = w(20, 20, 20)
        return dic_N[a, b, c]

    elif a < b and b < c:
        if (a, b, c-1) in dic_N: pass
        else:
            dic_N[a, b, c-1] = w(a, b, c-1)
        
        if (a, b-1, c-1) in dic_N: pass
        else:
            dic_N[a, b-1, c-1] = w(a, b-1, c-1)
        
        if (a, b-1, c) in dic_N: pass
        else:
            dic_N[a, b-1, c] = w(a, b-1, c)
        
        return dic_N[a, b, c-1] + dic_N[a, b-1, c-1] - dic_N[a, b-1, c]
    
    else:
        if (a-1, b, c) in dic_N: pass
        else:
            dic_N[a-1, b, c] = w(a-1, b, c)
        
        if (a-1, b-1, c) in dic_N: pass
        else:
            dic_N[a-1, b-1, c] = w(a-1, b-1, c)
        
        if (a-1, b, c-1) in dic_N: pass
        else:
            dic_N[a-1, b, c-1] = w(a-1, b, c-1)
            
        if (a-1, b-1, c-1) in dic_N: pass
        else:
            dic_N[a-1, b-1, c-1] = w(a-1, b-1, c-1)
            
        return dic_N[a-1, b, c] + dic_N[a-1, b-1, c] + dic_N[a-1, b, c-1] - dic_N[a-1, b-1, c-1]


dic_N = {}

while True:
    N = tuple(map(int, sys.stdin.readline().split()))

    if (N[0], N[1], N[2]) == (-1, -1, -1):
        break
    else:
        answer = w(N[0], N[1], N[2])
        print('w({}, {}, {}) = {}'.format(N[0], N[1], N[2], answer))
