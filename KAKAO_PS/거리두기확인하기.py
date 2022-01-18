'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.3MB)
테스트 8 〉	통과 (0.06ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.06ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.04ms, 10.3MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.04ms, 10.3MB)
테스트 17 〉	통과 (0.04ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (0.06ms, 10.4MB)
테스트 20 〉	통과 (0.04ms, 10.3MB)
테스트 21 〉	통과 (0.02ms, 10.2MB)
테스트 22 〉	통과 (0.04ms, 10.2MB)
테스트 23 〉	통과 (0.03ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.81ms, 10.4MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.04ms, 10.3MB)
테스트 29 〉	통과 (0.06ms, 10.4MB)
테스트 30 〉	통과 (0.03ms, 10.2MB)
'''
def dst_chk(i, j, place):
    
    direct_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    break_trigger = False
                
    for y_1, x_1 in direct_list:
        n_y_1 = i + y_1
        n_x_1 = j + x_1

        if len(place) > n_y_1 >= 0 and len(place[0]) > n_x_1 >= 0:
            if place[n_y_1][n_x_1] == 'X':
                continue
                
            if place[n_y_1][n_x_1] == 'P':
                return False

            if place[n_y_1][n_x_1] == 'O':

                for y_2, x_2 in direct_list:

                    n_y_2 = n_y_1 + y_2
                    n_x_2 =  n_x_1 + x_2
                    
                    if n_y_2 == i and n_x_2 == j:
                        continue

                    if len(place) > n_y_2 >= 0 and len(place[0]) > n_x_2 >= 0:
                        if place[n_y_2][n_x_2] == 'P':
                            return False
    return True


def rotation(place):
    for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] != 'P':
                    continue
                
                if not dst_chk(i, j, place):
                    return 0
                
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(rotation(place))
        
    return answer