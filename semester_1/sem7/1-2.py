from Vector import Vector

n = int(input('Number of dots: '))
data = []
for i1 in range(n):
    x, y, z = map(int, input().split())
    data.append(Vector(x, y, z, 1))
max_sq = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(i+2, len(data)):
            a = abs((data[i] - data[j]) @ (data[i] - data[k])) / 2
            if a > max_sq:
                max_sq = a
print(max_sq)

