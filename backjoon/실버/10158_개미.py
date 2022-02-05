w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

print(w - abs(w - (x + t)%(2*w)), h - abs(h - (y + t)%(2*h)))