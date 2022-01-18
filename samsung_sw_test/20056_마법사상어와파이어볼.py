from collections import defaultdict

N, M, K = map(int, input().split())

ball_lst = defaultdict(list)

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    ball_lst[r-1, c-1].append([m, s, d])

dir_lst = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def routine():

    global standard
    move_ball_lst = defaultdict(list)
    new_ball_lst = defaultdict(list)
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for point, balls in ball_lst.items():
        r, c = point
        for ball in balls:
            m, s, d = ball

            y = (r + s*dir_lst[d][0]) % N
            x = (c + s*dir_lst[d][1]) % N
            visited[y][x] += 1

            move_ball_lst[(y, x)].append([m, s, d])

    for point, balls in move_ball_lst.items():
        r, c = point
        if len(balls) >= 2:

            m = int(sum(map(lambda x: x[0], balls))/5)
            if m == 0:
                continue

            s = int(sum(map(lambda x: x[1], balls))/len(balls))

            same = True
            for i, ball in enumerate(balls):
                if i == 0:
                    standard = ball[2] % 2

                if ball[2]%2 == standard:
                    continue
                else:
                    same = False
                    break

            if same:
                for d in (0, 2, 4, 6):
                    new_ball_lst[(r, c)].append([m, s, d])
            else:
                for d in (1, 3, 5, 7):
                    new_ball_lst[(r, c)].append([m, s, d])
        else:
            new_ball_lst[(r, c)].append([balls[0][0], balls[0][1], balls[0][2]])
    return new_ball_lst

for _ in range(K):
    ball_lst = routine()

answer = 0
for point, balls in ball_lst.items():
    answer += sum(map(lambda x: x[0], balls))

print(answer)
