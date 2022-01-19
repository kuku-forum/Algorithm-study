'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.19ms, 10.2MB)
테스트 5 〉	통과 (1.44ms, 10.2MB)
테스트 6 〉	통과 (2.14ms, 12.8MB)
테스트 7 〉	통과 (2.37ms, 12.9MB)
테스트 8 〉	통과 (3.98ms, 12.8MB)
테스트 9 〉	통과 (21.09ms, 13.8MB)
테스트 10 〉	통과 (188.81ms, 21MB)
테스트 11 〉	통과 (170.96ms, 20.3MB)
테스트 12 〉	통과 (166.17ms, 20.4MB)
테스트 13 〉	통과 (176.93ms, 20.5MB)
'''
from collections import defaultdict

def find_sup(graph, name, cost):
    
    repayment = int(cost*0.1)
    my_money = cost - repayment
    profit_dic[name] += my_money
    
    if my_money == 0 or graph[name] == "center":
        return
    
    return find_sup(graph, graph[name], repayment)
    
    
def solution(enroll, referral, seller, amount):
    
    global profit_dic
    graph_dic = defaultdict(str)
    profit_dic = defaultdict(int)
    profit_dic['center'] = 0
    
    for enr, ref in zip(enroll, referral):
        if ref == "-":
            graph_dic[enr] = "center"
        else:
            graph_dic[enr] = ref
        
        profit_dic[enr] = 0
    
    
    for human, sale in zip(seller, amount):
        find_sup(graph_dic, human, sale*100)
    
    del profit_dic['center']
    
    return [cost for cost in profit_dic.values()]