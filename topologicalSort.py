from collections import defaultdict

class Vertex:
    def __init__(self, vertex, num):
        self.vertex = vertex
        self.number = num


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def calculateIndegree(self, vertex):
        count = 0
        for key, value in self.graph.items():
            if vertex in value:
                count += 1
        return count

    def topologicalSort(self):
        L = []
        vertexNums = []
        for key, value in self.graph.items():
            inCounter = self.calculateIndegree(key)
            if inCounter == 0:
                L.append(key)
        i = 0
        L.sort()
        while len(L) != 0:
            vertex = L.pop(0)
            i += 1
            vertexNums.append(Vertex(vertex, i))
            for e in self.graph[vertex]:
                vertexW = e
                inCount = self.calculateIndegree(vertexW) - 1
                if inCount == 0:
                    L.append(vertexW)
                    L.sort()
            del self.graph[vertex]

        if i == self.V:
            for element in vertexNums:
                print(element.vertex + ": " + str(element.number))
        else:
            print("G is not a DAG!!")




g = Graph(8)
g.addEdge("A", "D")
g.addEdge("A", "G")
g.addEdge("A", "C")
g.addEdge("B", "H")
g.addEdge("B", "F")
g.addEdge("C", "F")
g.addEdge("C", "B")
g.addEdge("D", "H")
g.addEdge("E", "H")
g.addEdge("F", "G")
# g.addEdge("D", "A")
# g.addEdge("D", "C")

g.topologicalSort()