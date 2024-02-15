from Vector import Vector

N = int(input('Количество точек:  '))
data = []
for i in range(N):
    print('Координаты через пробел:')
    x, y, z = map(int, input().split())
    print('Масса:')
    m = int(input())
    data.append(Vector(x, y, z, m))
center_mass = Vector(0, 0, 0, 0)
M = 0
for i in data:
    M += i.m
for i in data:
    i *= i.m
    center_mass += i/M
print(center_mass)
    
