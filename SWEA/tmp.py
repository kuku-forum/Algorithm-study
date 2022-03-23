from collections import defaultdict
from itertools import combinations

def solution(n, m, k, records):
    
    record_set = []
    for record in records:
        record_set.append(sorted(set(record)))
    # print(record_set)    
            
    answer = []
    total_pass_case = defaultdict(int)
    for combi in combinations([n for n in range(1, k+1)], len(set(records[0]))):
        # print('combi', combi)
        
        for c, record in enumerate(record_set):
            prev = 0
            c_prev = 0
            # print(record)
            pass_case = []
            for c, r in enumerate(record):
                # print(r, prev, combi[c])
                if r-prev >= combi[c]-c_prev:
                    prev = r
                    c_prev = combi[c]
                    pass_case.append(combi[c])
                else:
                    break
            else:
                # print(pass_case)
                total_pass_case[tuple(pass_case)] += 1
    
    len_record_set = len(record_set)
    for key in total_pass_case.keys():
        if total_pass_case[key] == len_record_set:
            answer.append(key)
            
    print(records)    
    print(answer)
    # print()
    # print(records[0])
    
    cnt_num = {}
    for i, j in enumerate(record_set[0]):
        cnt_num[j] = i
        
    print(cnt_num)
    print('answer', answer)
    
    # for recrod in records:
    target = []
    for r in records[0]:
        target.append(cnt_num[r])
    print(target)
    
    answer2 = []
    for row in answer:
        tmp = []
        for t in target:
            tmp.append(row[t])
        answer2.append(tmp)
        
    print('answer2', answer2)
    
    answer2.sort()
    print(answer2[-1])
    
    return answer2[-1]

# # 1312
solution(8, 4, 4, [[1,5,1,3], [5,7,5,6]])

# 1413
solution(8, 4, 4, [[1,5,1,3]])

# # 123
solution(10, 3, 3, [[1,2,3], [5,7,10]  ]) 

# # 0
# solution([[1, 2], [2, 3]], 
#          [[1, 3], [3, 2]], 
#          1)

# 1
# solution([[1, 2], [3, 1], [2, 4], [3, 5]], 
#          [[2, 1], [4, 1], [2, 5], [3, 2]], 
#          1)

# # 2
# solution([[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]], 
#          [[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]],
#          2)
