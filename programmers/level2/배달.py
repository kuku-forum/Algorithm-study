'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.4MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.60ms, 10.6MB)
테스트 15 〉	통과 (0.81ms, 10.6MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.03ms, 10.3MB)
테스트 18 〉	통과 (0.22ms, 10.3MB)
테스트 19 〉	통과 (0.77ms, 10.6MB)
테스트 20 〉	통과 (0.18ms, 10.3MB)
테스트 21 〉	통과 (0.96ms, 10.7MB)
테스트 22 〉	통과 (0.29ms, 10.4MB)
테스트 23 〉	통과 (0.94ms, 10.5MB)
테스트 24 〉	통과 (0.65ms, 10.6MB)
테스트 25 〉	통과 (1.53ms, 10.5MB)
테스트 26 〉	통과 (1.48ms, 10.7MB)
테스트 27 〉	통과 (1.76ms, 10.7MB)
테스트 28 〉	통과 (1.64ms, 10.6MB)
테스트 29 〉	통과 (1.61ms, 10.7MB)
테스트 30 〉	통과 (1.45ms, 10.7MB)
테스트 31 〉	통과 (0.05ms, 10.3MB)
테스트 32 〉	통과 (0.07ms, 10.3MB)
'''
import sys
from heapq import heappush, heappop

def dijkstra(graph, root, target):
    INF = sys.maxsize
    dst = [INF for _ in range(len(graph))]
    heap = []
    heappush(heap, root)
    cnt = 1
    
    while heap:
        wei, node = heappop(heap)
        if dst[node] < wei:
            continue
        
        for find_node, find_wei in graph[node]:
            sum_wei = find_wei + wei
            
            if dst[find_node] > sum_wei:
                dst[find_node] = sum_wei
                heappush(heap, (sum_wei, find_node))
    
    for d in dst[2:]:
        if target >= d:
            cnt += 1
    return cnt
        
    
def solution(N, road, K):
    answer = 0
    
    graph_lst = [[] for _ in range(N + 1)]
    
    for row in road:
        graph_lst[row[0]].append([row[1], row[2]])
        graph_lst[row[1]].append([row[0], row[2]])
    
    return dijkstra(graph_lst, (0, 1), K)

