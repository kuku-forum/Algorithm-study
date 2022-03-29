from my_package.hjtc import swea_tc

def babygin(arr):
    n_dic = {}
    
    for n in arr:
        if not n in n_dic:
            n_dic[n] = 1
        else:
            n_dic[n] += 1
            
            if n_dic[n] >= 3:
                return True
            
    keys = sorted(n_dic.keys())
    
    if len(keys) >= 3:
        for i in range(len(keys) - 2):
            if keys[i+1] - keys[i] == 1 and keys[i+2] - keys[i+1] == 1:
                return True
    return False


def solution():
    arr1 = []
    arr2 = []
    
    for i, n in enumerate(map(int, input().split())):
        if i%2 == 0:
            arr1.append(n) 
            if len(arr1) >= 3 and babygin(arr1):
                return 1
        else:
            arr2.append(n)
            if len(arr2) >= 3 and babygin(arr2):
                return 2
    return 0
    

for t in range(1, int(input()) + 1):
    print(f'#{t} {solution()}')