#решал все шахмтантые задачи, когда проходил условия...
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
ax = abs(x1 - x2)
ay = abs(y1 - y2)
if ax == 2 and ay == 1 or ax == 1 and ay == 2:
    print('YES')

else:
    print('NO')