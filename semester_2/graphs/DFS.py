class Graph:
    def __init__(self, edge_list, vert_num):
        self.adj_list = [[] for i in range(vert_num)]
        self.vert_num = vert_num
        for edge in edge_list:
            self.adj_list[edge[0]].append(edge[1])
        self.set_None()

    def set_None(self):
        self.colors = ['w' for i in range(self.vert_num)]
        self.timer = 0
        self.tin = [None for i in range(self.vert_num)]
        self.tout = [None for i in range(self.vert_num)]
        self.parents = [None for i in range(self.vert_num)]

    def dfs(self, vert_now):
        self.colors[vert_now] = 'g'
        self.timer += 1
        self.tin[vert_now] = self.timer
        for next_vert in self.adj_list[vert_now]:
            self.parents[next_vert] = vert_now
            
            if self.colors[next_vert] == 'g':
                cycle = [vert_now]
                cycle_vert = vert_now
                while cycle_vert != next_vert:
                    cycle_vert = self.parents[cycle_vert]
                    cycle.append(cycle_vert)
                print(f'found cycle: {cycle[::-1]}')
                continue

            elif self.colors[next_vert] == 'b':
                continue
            elif self.colors[next_vert] == 'w':
                self.dfs(next_vert)

        self.colors[vert_now] = 'b'
        self.timer += 1
        self.tout[vert_now] = self.timer

    def top_sort(self):
        self.set_None()
        for v in range(self.vert_num):
            if self.colors[v] == 'w':
                self.dfs(v)
        vert_list = [i for i in range(self.vert_num)]
        ans = [x for y, x in
                sorted(zip(self.tout, vert_list),
                    key=lambda pair: pair[0], reverse = True)]
        return ans

    def find_ways(self):
        self.set_None()
        ts_graph = self.top_sort()
        ways = [1 for i in range(self.vert_num)]
        for v in ts_graph[::-1]:
            for vert in self.adj_list[v]:
                ways[v] += ways[vert]
        return ways

edge_list_1 = [[0,1], [0,2], [0,3], [1,2], [1,4], [2,4], [3,4], [4,5], [5,3]]
graph_1 = Graph(edge_list_1, 6)
print('The first part: DFS')
graph_1.dfs(0)
print(f'colors: {graph_1.colors}')

edge_list_2 = [[0,1], [0,3], [1,3], [2,3], [4,3], [4,0], [5,0]]
graph_2 = Graph(edge_list_2, 6)
print('The second part: top sort')
print('top_sort: ', graph_2.top_sort())
print('ways: ', graph_2.find_ways())

