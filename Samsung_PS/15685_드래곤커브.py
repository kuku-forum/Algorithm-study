'''
오, 아래


0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)

 x, y, d, g
 좌표(x, y)
 방향: d
 세대: g
 
 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수
 
 3
3 3 0 1
4 2 1 3
4 2 2 1

board 만들기
direct_list()

1. rot 함수구하고
2. 4개의 제네레이선10세대까지 구하고
3. 매핑하고
4. conv 2*2 mat 
'''

