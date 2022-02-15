arr = [1, 2, 3, 4, 5]
n = 3
[1,2,3], [1,2 4]....[3,4,5]


# combi(arr[2, 3, 4, 5], 2)


# combi(arr[3, 4, 5], 1) 

# combi(arr[4, 5], 0) -> [[]]

element = 3
result += [element] + [[]]



# 1
combi(arr[3, 4, 5], 1)

def combi(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)): # 0, 1, 2
        #elem = arr[i] # 3
        elem = arr[1] # 4

        for C in combi(arr[i+1:], n-1):
        for C in combi(arr[5], 0):
        for C in [[]]:
            
            result += [[elem] + C]
            # result += [[3] +[]]
            # result += [[3]]
            # [] + [3]
            # [[3]]
            
    # return result # [[3]]
    return result # [[4]]


combi(arr[2, 3, 4, 5], 2)

def combi(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)): # 5: 0~5
        elem = arr[i] 
    
        # for C in  combi(arr[3, 4, 5], 1) :
        
        for C in  [[3]] :
            result += [[elem] + [3]]
            result += [[2] + [3]]
            result += [[2, 3]]
            [[2, 3]]
            
    return  [[2, 3]]


# combi(arr[1, 2, 3, 4, 5], 3)
def combi(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)): # 5: 0~5
        elem = arr[i] # arr[0] -> 1
        
        # for C in combi(arr[2, 3, 4, 5], 2):
        for C in [[2, 3]]:
            result += [[1] + [2, 3]]
            
    result = [[1, 2, 3]]
    
    return result
            
def combi(arr, n):
    result = []
    
    
    if n == 0:
        return [[]]
    
    for i in range(len(arr)): # 5: 0~5
        elem = arr[i] #2
        
        for C in combi(arr[i+1:], n-1):
            result += [[elem] + C]
            [[1, 2, 3]] + [[1, 2, 4]]
            
    # i = 0 결과, 한번 도니깐 result = [[1, 2, 3]] 
    # [1, 2, 4]       
    # [[1, 2, 3], [1, 2, 4], [1, 2, 5]...
    # [1,4,5], [2,3,4]]
    return result