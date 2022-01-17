import heapq
from graph import Graph

def primsAlgorithm(graph, startNode):
    heap = []

    if(isinstance(startNode, str)):
        startNode = graph.getVertices(startNode)

    for vertex in graph.getVertices():
        weight = float('inf')
        if(vertex == startNode):
            weight = 0
        
        heap.append((weight,vertex.value))

    heapq.heapify(heap)
    weights = {}
    paths = {}
    tree = Graph()

    while(len(heap) > 0):
        dequeued = heapq.heappop(heap)
        weights[dequeued[1]] = dequeued[0]

        currentVertex = graph.getEdges(dequeued[1])

        while(currentVertex != None):
            value = next((x for x in heap if currentVertex.value.value == x[1]), None)
            if(not value):
                currentVertex = currentVertex.nextAdj
                continue
            adjIndex = heap.index(value)
            if(heap[adjIndex][0] > currentVertex.weight):
                paths[heap[adjIndex][1]] = dequeued[1]
                heap[adjIndex] = (currentVertex.weight, heap[adjIndex][1])

            currentVertex = currentVertex.nextAdj
        
        heapq.heapify(heap)
    
    currentVertex = list(paths.keys())[len(paths.keys()) - 1]

    
    for vertex in graph.getVertices():
        tree.insertVertex(vertex)
        
    for currentVertex in paths.keys():
        tree.insertEdge(currentVertex, paths[currentVertex], weights[currentVertex])

    return tree
