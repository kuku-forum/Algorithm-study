'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
'''
def find(target):
    if target == parent[target]:
        return target
    
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    
    global parent
    parent = [i for i in range(n)]
    answer = 0
    line_chk = 0
    costs.sort(key = lambda x: x[2])
    
    for start, end, cost in costs:
        if line_chk == n - 1:
            break
            
        if find(start) == find(end):
            continue
            
        union(start, end)
        line_chk += 1
        answer += cost
    
    return answer