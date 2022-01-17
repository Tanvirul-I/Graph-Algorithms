import heapq

def dijkstrasAlgorithm(graph, startNode, endNode):
    heap = []

    if(isinstance(startNode, str)):
        startNode = graph.getVertices(startNode)

    if(isinstance(endNode, str)):
        endNode = graph.getVertices(endNode)

    for vertex in graph.getVertices():
        weight = float('inf')
        if(vertex == startNode):
            weight = 0
        
        heap.append((weight,vertex.value))

    heapq.heapify(heap)
    weights = {}
    paths = {}
    path = [endNode.value]

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
            if(heap[adjIndex][0] > dequeued[0] + currentVertex.weight):
                paths[heap[adjIndex][1]] = dequeued[1]
                heap[adjIndex] = (dequeued[0] + currentVertex.weight, heap[adjIndex][1])

            currentVertex = currentVertex.nextAdj
        
        heapq.heapify(heap)

    currentVertex = paths[endNode.value]

    while(currentVertex != startNode.value):
        path.append(currentVertex)
        currentVertex = paths[currentVertex]
        
    path.append(startNode.value)
    path.reverse()

    return path
    