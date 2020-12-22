# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys  # Library for INT_MAX

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

        # A utility function to print the constructed MST stored in parent[]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(alpha[parent[i]], "-", alpha[i], "\t", self.graph[i][parent[i]])

            # A utility function to find the vertex with

    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

        # Function to construct and print MST for a graph

    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[7] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)



g = Graph(8)

          # A  B  C  D  E  F  G  H
          # 0  1  2  3  4  5  6  7
g.graph = [[0, 43, 89, 69, 0, 0, 0, 0], #A 0
           [43, 0, 53, 0, 84, 0, 0, 0], #B 1
           [89, 53, 0, 23, 72, 78, 40, 0], #C 2
           [69, 0, 23, 0, 0, 0, 68, 0], #D 3
           [0, 84, 72, 0, 0, 96, 0, 62], #E 4
           [0, 0, 78, 0, 96, 0, 26, 94], #F 5
           [0, 0, 40, 68, 0, 26, 0, 85], #G 6
           [0, 0, 0, 0, 62, 94, 85, 0]] #H 7
# g = Graph(11)
#
#           # A  B  C  D  E  F  G  H
#           # 0  1  2  3  4  5  6  7
# g.graph = [[0, 43, 89, 69, 0, 0, 0, 0, 0], #A 0
#            [43, 0, 53, 0, 84, 0, 0, 0, 0, 0, 0], #B 1
#            [0, 6, 0, 5, 0, 0, 0, 12, 0, 0, 0], #C 2
#            [0, 0, 5, 0, 7, 0, 0, 0, 0, 0, 0], #D 3
#            [0, 0, 0, 7, 0, 5, 0, 6, 0, 0, 0], #E 4
#            [9, 0, 0, 0, 5, 0, 2, 0, 0, 0, 0], #F 5
#            [0, 3, 0, 0, 0, 2, 0, 4, 0, 0, 0], #G 6
#            [0, 0, 12, 0, 6, 0, 4, 0, 0, 0, 0], #H 7
#            [19, 0, 0, 0, 0, 0, 0, 0, 0, 14, 12], #I 8
#            [0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 9], #J 9
#            [0, 0, 0, 0, 0, 0, 0, 0, 12, 9, 0]] #K 10

g.primMST();

# Contributed by Divyanshu Mehta






