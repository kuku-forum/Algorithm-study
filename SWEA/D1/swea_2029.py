T = int(input())

for i in range(1, T+1):
    num1, num2 = map(int, input().split())
    q, r = divmod(num1, num2)
    print(f'#{i} {q} {r}')