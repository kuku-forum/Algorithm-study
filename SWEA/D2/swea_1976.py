T = int(input())

for t in range(1, T + 1):
    
    h1, m1, h2, m2 = map(int, input().split())
    
    h = h1 + h2
    m_q, m = divmod((m1 + m2), 60)
    h += m_q
    
    while h > 12:
        h -= 12
    
    print(f'#{t}', h, m)