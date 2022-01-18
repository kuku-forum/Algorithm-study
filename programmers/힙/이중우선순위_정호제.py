'''정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.5MB)
'''
import heapq

def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    
    for op in operations:
        com, num = op.split()
        if com == 'I':
            heapq.heappush(max_heap, (-int(num), int(num)))
            heapq.heappush(min_heap, (int(num), int(num)))
        elif com == 'D':
            if not max_heap:
                continue
                
            if int(num) == 1:
                max_value = heapq.heappop(max_heap)
                min_heap.remove((-max_value[0], max_value[1]))
                
            else:
                min_value = heapq.heappop(min_heap)
                max_heap.remove((-min_value[0], min_value[1]))
        
    
    if not max_heap:
        return [0, 0]
    else:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)[1]]