class Vector():
    def __init__(self, x, y, z, m):
        self.x = x
        self.y = y
        self.z = z
        self.m = m
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)**0.5
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z, self.m)
        elif isistance(other, int) or isistanse(other, float):
            return Vector(self.x + other, self.y + other, self.z + other, self.m)
    def __radd__(self, other):
        return self + other
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other, self.m)
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other, self.z / other, self.m)

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
    
