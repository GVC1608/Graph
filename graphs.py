class Graph:
    def __init__(self, dict=None):
        if dict is None:
            self.dict = {}
        self.dict = dict

    def addEdge(self, vertex, edge):
        self.dict[vertex].append(edge)

    def addVertex(self, vertex):
        if vertex not in self.dict.keys():
            self.dict[vertex] = []
        else:
            print("vertex is already added")

    def removeVertex(self, vertex):
        if vertex not in self.dict.keys():
            print("{} vertex is not in graph".format(vertex))
        else:
            for i in self.dict[vertex]:
                self.dict[i].remove(vertex)
            self.dict.pop(vertex)
            print("successfully remove the vertex {}".format(vertex))

    def removeEdge(self, vertexA, vertexB):
        if vertexA not in self.dict.keys() or vertexB not in self.dict.keys():
            print(" specified vertices is missing")
        else:
            self.dict[vertexA].remove(vertexB)
            self.dict[vertexB].remove(vertexA)

    def printGraph(self):
        print(self.dict)

def find_shortest_distance(vertex1, vertex2, pathcost=0):
	"""
		finding the shortest distance using dijkastra algo
	"""
	pass

customgraphdict = {
    "A":["B", "C"],
    "B":["D","E","A"],
    "D":["E", "F","B"],
    "F":["D","E"],
    "E":["B","D","C"],
    "C":["A","E"]
}

g = Graph(customgraphdict)
g.addVertex("G")
g.addEdge("G","D")
g.addEdge("D", "G")
g.removeEdge("A", "B")
g.printGraph()