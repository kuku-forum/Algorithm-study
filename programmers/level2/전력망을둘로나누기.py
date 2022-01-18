'''
정확성  테스트
테스트 1 〉	통과 (3.32ms, 10.3MB)
테스트 2 〉	통과 (3.29ms, 10.3MB)
테스트 3 〉	통과 (2.52ms, 10.3MB)
테스트 4 〉	통과 (3.42ms, 10.3MB)
테스트 5 〉	통과 (2.92ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.17ms, 10.2MB)
테스트 9 〉	통과 (0.14ms, 10.3MB)
테스트 10 〉	통과 (2.65ms, 10.3MB)
테스트 11 〉	통과 (3.36ms, 10.3MB)
테스트 12 〉	통과 (4.98ms, 10.4MB)
테스트 13 〉	통과 (2.71ms, 10.3MB)
'''
from collections import defaultdict, deque

def bfs(root, tree, n):
    v1 = root[0]
    v2 = root[1]
    
    que1 = deque([v1])
    que2 = deque([v2])
    visited1 = [0 for _ in range(n+1)]
    visited2 = [0 for _ in range(n+1)]
    
    while que1:
        parent = que1.popleft()
        visited1[parent] = 1
        
        for child in tree[parent]:
            if child != v2 and visited1[child] == 0:
                que1.append(child)
    
    while que2:
        parent = que2.popleft()
        visited2[parent] = 1
        
        for child in tree[parent]:
            if child != v1 and visited2[child] == 0:
                que2.append(child)

    return abs(sum(visited1) - sum(visited2))
    

def solution(n, wires):
    answer = 0xffff
    tree_lst = defaultdict(list)
    
    for v1,v2 in wires:
        tree_lst[v1].append(v2)
        tree_lst[v2].append(v1)
    
    for wire in wires:
        answer = min(answer, bfs(wire, tree_lst, n))
            
    return answer