from collections import deque

N, K = map(int, input().split())
belt_lst = deque([])

for elem in map(int, input().split()):
    belt_lst.append([elem, 0])

def run(belt):
    stop = 0
    cnt = 0

    while True:
        cnt += 1
        belt.rotate(1)
        if belt[N-1][1] >= 1:
            belt[N-1][1] = 0


        for i in range(N-2, -1, -1):
            # print(i)
            if belt[i][1] >= 1 and belt[i+1][1] == 0 and belt[i+1][0] >= 1:
                # move
                belt[i+1][1] += 1
                belt[i+1][0] -= 1
                belt[i][1] = 0

                if belt[i+1][0] == 0:
                    stop += 1

        if belt[N-1][1] >= 1:
            belt[N-1][1] = 0

        if belt[0][1] == 0 and belt[0][0] >= 1:
            belt[0][1] += 1
            belt[0][0] -= 1

            # put
            if belt[0][0] == 0:
                stop += 1

        # print(belt, stop, cnt)
        if stop >= K:
            return cnt




answer = run(belt_lst)
print(answer)

