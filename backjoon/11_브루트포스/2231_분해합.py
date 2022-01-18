import sys

def div_sum(num):
    start_num = num//2
    
    for e_val in range(start_num, num):
        factor = [int(i) for i in str(e_val)]
        if num == (e_val + sum(factor)):
            return e_val
    return 0
        
T = int(sys.stdin.readline())
result = div_sum(T)
print(result)


