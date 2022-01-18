'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10MB)
테스트 12 〉	통과 (0.09ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
'''
def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        tree = list(tree)
        order_lst = []
        tri = True

        for order in skill:
            if order in tree:
                order_lst.append(str(tree.index(order)))
            else:
                order_lst.append(order)
        # print(order_lst)

        while True:
            if not order_lst:
                break

            if order_lst[-1].isdigit():
                break
            elif order_lst[-1].isalpha():
                order_lst.pop()
        # print(order_lst)

        for i in range(1, len(order_lst)):
            tmp1 = order_lst[i-1]
            tmp2 = order_lst[i]
            # print(tmp1, tmp2)

            if tmp1.isalpha() or tmp2.isalpha():
                tri = False
                break

            if tmp1 > tmp2:
                tri = False
                break
        if tri:
            answer += 1

    return answer