import time

x = 100
y = 100

answer = 0

h = 0
start = time.time()  
while max(x, y)/2 >= h:
    answer = max(answer, (x - 2*h)*(y-2*h)*h)
    h += 0.000001
    
print(round(answer,6))

end = (time.time() - start)
print(f'time:{round(end, 3)} sec')