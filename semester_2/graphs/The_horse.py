inf = float('inf')
# The first coordinate is column

def Find_way(N, i, j, x, y):
    if (x,y) == (i,j): return (x,y)
    dist = [inf for k in range(N*N)]
    dist[i + N * j] = 0
    queue = []
    used = set()
    queue.append(i + N * j)
    prev = [None for k in range(N*N)]
    while queue:
        cur_vert = queue.pop(0)
        for next_vert in opport_for_move(N, cur_vert):
            if next_vert in used: continue
            used.add(next_vert)
            queue.append(next_vert)
            dist[next_vert] = dist[cur_vert] + 1
            prev[next_vert] = (cur_vert % N, cur_vert // N)
            if next_vert == x + y * N:
                way = []
                prev_vert = prev[next_vert]
                while prev_vert != (i,j):
                    way.insert(0, prev_vert)
                    prev_vert = prev[prev_vert[0] + N * prev_vert[1]]
                return way
    return 'no way'

def opport_for_move(N, cur_vert):
    x = cur_vert % N
    y = cur_vert // N
    answ = []
    for dest_x, dest_y in [(x - 1, y - 2), (x + 1, y - 2),
            (x - 2, y - 1), (x + 2, y - 1),
            (x - 2, y + 1), (x + 2, y + 1),
            (x - 1, y + 2), (x + 1, y + 2)]:
        if not (dest_x < 0 or dest_y < 0 or
                dest_x > N - 1 or dest_y > N - 1):
            answ.append(dest_x + dest_y * N)
    return answ

N = int(input())
i, j = map(int, input().split())
x, y = map(int, input().split())
print(Find_way(N, i, j, x, y))
