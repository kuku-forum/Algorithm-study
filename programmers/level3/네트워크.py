
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.14ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.10ms, 10.4MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
테스트 11 〉	통과 (0.40ms, 10.3MB)
테스트 12 〉	통과 (0.40ms, 10.3MB)
테스트 13 〉	통과 (0.16ms, 10.2MB)
'''
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    
    for i, computer in enumerate(computers):
        for target, connect in enumerate(computer):
            if connect == 1:
                graph[i].append(target)
                
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        stack = [i]
        if visited[i] == 1:
            continue
            
        while stack:
            node = stack.pop()
            
            for new_node in graph[node]:
                if visited[new_node] == 1:
                    continue
                    
                visited[new_node] = 1
                stack.append(new_node)
        
        answer += 1

    return answer
