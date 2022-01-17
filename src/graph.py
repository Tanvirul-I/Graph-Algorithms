from vertex import VertexAdj
from vertex import Vertex

class Graph:
    def __init__(self, vertices = None, directed = False):
        if(vertices != None):
            self.vertices = vertices
        else:
            self.vertices = []
        
        self.adjList = {}

        for vertex in self.vertices:
            self.adjList[vertex.value] = None

        self.directed = directed

    def insertVertex(self, vertex):
        self.vertices.append(vertex)
        self.adjList[vertex.value] = None

    def getVertices(self, match = None):
        if(match == None):
            return self.vertices
        else:
            return next((x for x in self.vertices if match == x or (isinstance(match, str) and match == x.value)), None)

    def insertEdge(self, vertex1, vertex2, weight):
        if(isinstance(vertex1, Vertex) == False): 
            vertex1 = self.getVertices(vertex1)

        if(isinstance(vertex2, Vertex) == False): 
            vertex2 = self.getVertices(vertex2)

        vertex1Head = VertexAdj(vertex2, None, weight)
        vertex1Head.nextAdj = self.adjList[vertex1.value]
        self.adjList[vertex1.value] = vertex1Head

        if(self.directed == False):
            vertex2Head = VertexAdj(vertex1, None, weight)
            vertex2Head.nextAdj = self.adjList[vertex2.value]
            self.adjList[vertex2.value] = vertex2Head

    def getEdges(self, vertex = None):
        if(vertex == None):
            return self.adjList
        elif(isinstance(vertex, Vertex) == False): 
            vertex = self.getVertices(vertex)

        return self.adjList[vertex.value]