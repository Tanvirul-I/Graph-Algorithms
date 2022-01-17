from vertex import Vertex
from graph import Graph
from dijkstras import dijkstrasAlgorithm
from prims import primsAlgorithm

def mainDij():
    vertex0 = Vertex("s")
    vertex1 = Vertex("t")
    vertex2 = Vertex("u")
    vertex3 = Vertex("v")
    vertex4 = Vertex("w")

    graph1 = Graph([vertex0, vertex1, vertex2, vertex3, vertex4], True)

    graph1.insertEdge(vertex0, vertex1, 10)
    graph1.insertEdge(vertex0, vertex3, 5)

    graph1.insertEdge(vertex1, vertex2, 1)
    graph1.insertEdge(vertex1, vertex3, 2)

    graph1.insertEdge(vertex2, vertex4, 4)

    graph1.insertEdge(vertex3, vertex1, 3)
    graph1.insertEdge(vertex3, vertex2, 9)
    graph1.insertEdge(vertex3, vertex4, 2)

    graph1.insertEdge(vertex4, vertex2, 6)
    graph1.insertEdge(vertex4, vertex0, 7)

    print(dijkstrasAlgorithm(graph1, "s", "u"))

def mainPrim():
    vertex0 = Vertex("a")
    vertex1 = Vertex("b")
    vertex2 = Vertex("c")
    vertex3 = Vertex("d")
    vertex4 = Vertex("e")
    vertex5 = Vertex("f")
    vertex6 = Vertex("g")
    vertex7 = Vertex("h")
    vertex8 = Vertex("i")

    graph1 = Graph([vertex0, vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8])

    graph1.insertEdge(vertex0, vertex1, 4)
    graph1.insertEdge(vertex0, vertex7, 8)

    graph1.insertEdge(vertex1, vertex2, 8)
    graph1.insertEdge(vertex1, vertex7, 11)

    graph1.insertEdge(vertex2, vertex3, 7)
    graph1.insertEdge(vertex2, vertex5, 4)
    graph1.insertEdge(vertex2, vertex8, 2)

    graph1.insertEdge(vertex3, vertex4, 9)
    graph1.insertEdge(vertex3, vertex5, 14)

    graph1.insertEdge(vertex4, vertex5, 10)

    graph1.insertEdge(vertex5, vertex6, 2)

    graph1.insertEdge(vertex6, vertex7, 1)
    graph1.insertEdge(vertex6, vertex8, 6)

    graph1.insertEdge(vertex7, vertex8, 7)

    print(primsAlgorithm(graph1, "a").getEdges())

mainDij()
mainPrim()