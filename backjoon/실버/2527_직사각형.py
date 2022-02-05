box_list_1 = []
box_list_2 = []

for _ in range(4):
    square = list(map(int, input().split()))
    box_list_1.append(square[:4])
    box_list_2.append(square[4:])
    
answer = []

for box1, box2 in zip(box_list_1, box_list_2):
    x1, y1, p1, q1 = box1[0], box1[1], box1[2] ,box1[3]
    x2, y2, p2, q2 = box2[0], box2[1], box2[2] ,box2[3]
    
    if q1 < y2 or q2 < y1 or x1 > p2 or p1 < x2:
        answer.append('d')
    elif p1 == x2:
        answer.append('c' if q1 == y2 or y1 == q2 else 'b')
        
    elif x1 == p2:
        answer.append('c' if q1 == y2 or y1 == q2 else 'b')

    elif q1 == y2:
        answer.append('c' if x2 == p1 or p2 == x1 else 'b')
        
    elif q2 == y1:
        answer.append('c' if x2 == p1 or p2 == x1 else 'b')
        
    else:
        answer.append('a')
        
        
for result in answer:
    print(result)