def solution(name):
    
    alp_dic = {chr(alpha) : i for i, alpha in enumerate(range(ord('A'), ord('N')+1))}
    alp_dic.update({chr(alpha) : i+1 for i, alpha in enumerate(range(ord('Z'), ord('N'), -1))})
    
    answer = 0
    for i in name:
        answer += alp_dic[i]
    
    id_lst, rid_lst = [], []
    
    
    if 'A' not in name:
        return answer + len(name) - 1
    
    for i, alp in enumerate(name):
        if alp != 'A':
            if i == 0:
                continue
            id_lst.append(i)
            rid_lst.append(len(name)-i)
    
    tmp = []
    if 2 >= len(id_lst):
        return min(id_lst[-1], rid_lst[0]) + answer
    else:
        for i in range(len(id_lst) - 1):
            tmp.append( (2 * id_lst[i]) + (len(name) - id_lst[i + 1]))
        return min(id_lst[-1], rid_lst[0], min(tmp)) + answer