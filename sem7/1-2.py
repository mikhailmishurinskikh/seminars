#Среди данных точек найдите три точки, образующие треугольник с наибольшей площадью. Выведите данную площадь.
class Vector():
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        def __abs__(self):
            return (self.x**2 + self.y**2 + self.z**2)**0.5
        def __add__(self, other):
            if isinstance(other, Vector):
                return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
            elif isinstance(other, int) or isinstance(other, float):
                return Vector(self.x+other,self.y+other,self.z+other)
        def __radd__(self, other):
            return self + other
        def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        def __str__(self):
            return f'x = {self.x} y = {self.y} z = {self.z}'
        def __matmul__(self, other): #a @ b
            return Vector(
                    self.y * other.z - other.y * self.z, 
                    self.z * other.x - other.z * self.x,
                    self.x * other.y - other.x * self.y)
n = int(input('Number of dots: '))
data = []
for i1 in range(n):
    x, y, z = map(int, input().split())
    data.append(Vector(x, y, z))
max_sq = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(i+2, len(data)):
            a = abs((data[i] - data[j]) @ (data[i] - data[k])) / 2
            if a > max_sq:
                max_sq = a
print(max_sq)

