from collections import defaultdict

def find_sup(graph, name):
    name.append(graph[name[-1]])
    # print(name)
    if name[-1] == "center":
        return name
    
    return find_sup(graph, name)
    
    
def solution(enroll, referral, seller, amount):
    
    answer = []
    graph_dic = defaultdict(str)
    profit_dic = defaultdict(int)
    
    for enr, ref in zip(enroll, referral):
        if ref == "-":
            graph_dic[enr] = "center"
        else:
            graph_dic[enr] = ref
        
        profit_dic[enr] = 0
    
    print(graph_dic)
    for human, sale in zip(seller, amount):
        network = find_sup(graph_dic, [human])
        profit = sale*100
        
        for node in network:
            repayment = int(profit*0.1)
            # repayment = profit//10
            profit_dic[node] += profit - repayment
            profit = repayment
    
    
    del profit_dic['center']
    
    return [cost for cost in profit_dic.values()]


a = ["john"]
b = ["-"]
c = ["john"]
d = [10]

a = solution(a, b, c, d)
print(a)