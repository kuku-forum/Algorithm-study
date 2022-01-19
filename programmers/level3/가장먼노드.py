
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.18ms, 10.3MB)
테스트 5 〉	통과 (0.62ms, 10.5MB)
테스트 6 〉	통과 (1.87ms, 10.9MB)
테스트 7 〉	통과 (14.86ms, 17MB)
테스트 8 〉	통과 (27.30ms, 20.5MB)
테스트 9 〉	통과 (23.78ms, 20.3MB)
'''
from collections import deque, Counter

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    print(graph)
        
    visited = [-1 for _ in range(n+1)]
    visited[1] = 0
    que = deque([1])
    
    while que:
        node = que.popleft()
        print(visited)
        
        for target in graph[node]:
            if visited[target] == -1:
                visited[target] = visited[node] + 1
                que.append(target)
    
    visited.sort(reverse = True)
    max_value = visited[0]
    
    answer = 0
    for val in visited:
        if max_value == val:
            answer += 1
        else:
            break
    return answer