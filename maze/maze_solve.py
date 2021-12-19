from collections import defaultdict
import argparse


class Graph:

    # Default dict to store Graph
    def __init__(self):

        self.graph = defaultdict(list)
        self.edges = {}
        self.prev_vertex = {}

# adding an Edge
    def add_edge(self, u, v, weight=1):

        self.graph[u].append(v)
        self.graph[v].append(u)

        self.edges[(u, v)] = weight
        self.edges[(v, u)] = weight

# By using BFS it checkes path exist in node or not
    def isConnected(self, u, v):

        visted = {}
        for i in self.graph:
            visted[i] = False

        queue = []
        queue.append(u)
        connected_vertices = set()

        while queue:
            temp = queue.pop(0)
            connected_vertices.add(temp)
            visted[temp] = True
            for i in self.graph[temp]:
                if (visted[i] is False):
                    queue.append(i)

        if u in connected_vertices and v in connected_vertices:
            return True
        return False

# Using Dijkastra Finding the shortest path Using source and destination
    def dijkstra(self, node):
        dist = {}
        vertex = {}
        for i in self.graph:
            if i == node:
                dist[(node, i)] = 0
            else:
                dist[(node, i)] = 10**9
        for i in self.graph:
            vertex[i] = False
        temp = node
        while vertex[temp] is False:
            vertex[temp] = True
            for i in self.graph[temp]:
                if (vertex[i] is False
                    and dist[(node, i)] > self.edges[(temp, i)]
                        + dist[(node, temp)]):
                    dist[(node, i)] = self.edges[(temp, i)]
                    + dist[(node, temp)]
                    self.prev_vertex[i] = temp
            temp_dict = {}
            for i in self.graph[temp]:
                temp_dict[i] = dist[(node, i)]
            temp_dict = sorted(temp_dict.items())

            for i in range(len(temp_dict)):
                if vertex[temp_dict[i][0]] is False:
                    temp = temp_dict[i][0]
                    break
            else:
                if vertex[self.prev_vertex[temp]] is False:
                    temp = self.prev_vertex[temp]
                else:
                    min_dist = 10**9
                    for i in self.graph:
                        if vertex[i] is False and dist[(node, i)] < min_dist:
                            temp = i
                            break
        return self.prev_vertex

# Finding privious vertex set from source to destination

    def src_to_dest(self, u, v):

        if self.isConnected(u, v) is True:

            prev_vertex = self.dijkstra(u)
            prev_vertex = list(prev_vertex.items())
            size = len(prev_vertex)
            src_to_dest = []
            temp = v

            while temp:
                src_to_dest.insert(0, temp)
                if temp == u:
                    break
                for i in range(size):
                    if prev_vertex[i][0] == temp:
                        temp = prev_vertex[i][1]

            src_to_dest = set(src_to_dest)

            return src_to_dest
        else:
            return -1

#-----------------------------------------------------DRIVER CODE---------------------------------------------------------

g = Graph()

pars = argparse.ArgumentParser()
pars.add_argument('ip_file', help='Input File')
pars.add_argument('op_file', help='Output File')
pars.add_argument('--s', '--sourece', help='add destination')
pars.add_argument('--d', '--destination', help='add source')
arg = pars.parse_args()

