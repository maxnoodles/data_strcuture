# 顶点类
class Vertex:

    def __init__(self, name):
        self.name = name
        self.connectTo = {}
        self.mark = 0

    def add_neighbor(self, nbr, weight=0):
        self.connectTo[nbr] = weight

    def __str__(self):
        return str(self.name) + 'connectTo' + str([x.name for x in self.connectTo])

    def get_connection(self):
        return self.connectTo.keys()

    def get_name(self):
        return self.name

    def get_weight(self, nbr):
        return self.connectTo[nbr]


class Graph:

    def __init__(self):
        self.ver_dir = {}
        self.num_vertex = 0

    def add_vertex(self, name):
        self.num_vertex += 1
        vertex = Vertex(name)
        self.ver_dir[name] = vertex
        return vertex

    def get_vertex(self, name):
        if name in self.ver_dir:
            return self.ver_dir[name]
        else:
            return None

    def __contains__(self, item):
        return item in self.ver_dir

    def addEdge(self, fst, snd, weight=0):
        if fst not in self.ver_dir:
            self.ver_dir[fst] = Vertex(fst)
        if snd not in self.ver_dir:
            self.ver_dir[snd] = Vertex(snd)
        self.ver_dir[fst].add_neighbor(self.ver_dir[snd], weight)

    def get_vertexs(self):
        return self.ver_dir.keys()

    def __iter__(self):
        return iter(self.ver_dir.values())

    def dfsmian(self):
        k = 0
        def dfs(name):
            print(name.get_name(), k)
            name.mark = 1
            p = name.get_connection()
            for i in p:
                # i = i.name
                if i.mark == 0:
                    dfs(i)

        for x in self.ver_dir.values():
            if x.mark == 0:
                k += 1
                dfs(x)

    def bfs(self):
        list = []
        for x in self.ver_dir.keys():
            if self.ver_dir[x].mark == 0:
                print(x, x)
                self.ver_dir[x].mark = 1
                for i in self.ver_dir[x].get_connection():
                    # i = i.name
                    # if self.ver_dir[i].mark == 0:
                    #     print(i)
                    #     self.ver_dir[i].mark = 1
                    if i.mark == 0:
                        print(i.name)
                        i.mark = 1

def test_graph():
    graph = Graph()
    for i in range(1,9):
        graph.add_vertex(i)
    graph.addEdge(1, 2, 3)
    graph.addEdge(1, 3, 4)
    graph.addEdge(1, 4, 5)
    graph.addEdge(2, 1, 3)
    graph.addEdge(2, 3, 5)
    graph.addEdge(2, 4, 6)
    graph.addEdge(3, 1, 4)
    graph.addEdge(3, 2, 5)
    graph.addEdge(3, 5, 8)
    graph.addEdge(4, 1, 5)  # E
    graph.addEdge(4, 2, 6)
    graph.addEdge(5, 2, 7)
    graph.addEdge(5, 4, 9)
    graph.addEdge(6, 7, 13)
    graph.addEdge(6, 8, 14)
    graph.addEdge(7, 6, 13)
    graph.addEdge(7, 8, 15)
    graph.addEdge(8, 6, 14)
    graph.addEdge(8, 7, 15)
    return graph


graph1 = test_graph()
# graph1.bfs()
graph1.dfsmian()
# for i in graph1:
    # print(i)
