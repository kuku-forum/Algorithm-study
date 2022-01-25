N, K = map(int, input().split())

person = [[0, 0] for _ in range(7)]

for _ in range(N):
    Y, S = map(int, input().split())
    person[S][Y] += 1
    
answer = 0
for y in range(1, 7):
    q, r = divmod(person[y][0], K)
    if r == 0:
        answer += q
    else:
        answer += q + 1
        
    q, r = divmod(person[y][1], K)
    if r == 0:
        answer += q
    else:
        answer += q + 1
        
print(answer)