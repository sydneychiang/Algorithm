# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph


# Library for INT_MAX
import sys

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.parent = {}
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Dijkstra's Algorithm")
        print("Vertex \t Distance \t Parent")
        # print("%s %10s %10s"%("Vertex","Distance from Source","parent"))
        for node in range(self.V):
            if(dist[node] == 0):
                parentNode = "-"
            else:
                parentNode = self.parent[alpha[node]]
            print("%2s %10d %10s"%(alpha[node], dist[node], parentNode))

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                    self.parent[alpha[v]] = alpha[u]
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Driver program
g = Graph(8)

          # A  B  C  D  E  F  G  H
          # 0  1  2  3  4  5  6  7
g.graph = [[0, 12, 21, 26, 0, 0, 0, 0], #A 0
           [12, 0, 27, 0, 3, 0, 0, 0], #B 1
           [21, 27, 0, 16, 5, 3, 11, 0], #C 2
           [26, 0, 16, 0, 0, 0, 25, 0], #D 3
           [0, 3, 5, 0, 0, 19, 0, 4], #E 4
           [0, 0, 3, 0, 19, 0, 23, 7], #F 5
           [0, 0, 11, 25, 0, 23, 0, 10], #G 6
           [0, 0, 0, 0, 4, 7, 10, 0]] #H 7


          # A  B  C  D  E  F  G  H  I  J
          # 0  1  2  3  4  5  6  7  8  9
# g.graph = [[0, 12, 21, 26, 0, 0, 0, 0, 0, 0], #A 0
#            [12, 0, 27, 0, 3, 0, 0, 0, 0, 0], #B 1
#            [21, 27, 0, 16, 5, 3, 11, 0, 0, 0], #C 2
#            [7, 0, 6, 0, 0, 0, 1, 0, 0, 0], #D 3
#            [0, 15, 5, 0, 0, 6, 0, 9, 10, 0], #E 4
#            [0, 0, 2, 0, 6, 0, 6, 10, 0, 0], #F 5
#            [0, 0, 4, 1, 0, 6, 0, 6, 0, 9], #G 6
#            [0, 0, 0, 0, 9, 10, 6, 0, 2, 5], #H 7
#            [0, 0, 0, 0, 10, 0, 0, 2, 0, 12], #I 8
#            [0, 0, 0, 0, 0, 0, 9, 5, 12, 0]] #J 9

g.dijkstra(0)

# This code is contributed by Divyanshu Mehta
