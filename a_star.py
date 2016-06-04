import heapq
import geometry

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class node:
    def __init__(self):
        self.hScore = 0
        self.stepCost = 0
        self.fScore = 0
        self.childIndexes = []
        self.index = -1
        self.camerasState = [True]*geometry.Gallery.camerasAmount
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.fScore == other.fScore
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.fScore< other.fScore
    def expand(self):
        (self.childIndexes,self.hScore) = geometry.getIndexOfCamerasToTurnOff(self.camerasState,self.index)
        self.fScore = self.stepCost + self.hScore


def aStar(cameras):
    root = node()
    if not geometry.isGalleryCovered(root.camerasState):
        return None
    root.expand()
    nodesQueueByFScore = PriorityQueue()
    nodesQueueByFScore.put(root,-root.fScore*1000 - root.stepCost)

    while not nodesQueueByFScore.empty():
        currentNode = nodesQueueByFScore.get()
        if currentNode.hScore == 0:
            return currentNode

        for (i,childIndex) in enumerate(currentNode.childIndexes):

            newNode = node()
            newNode.stepCost = currentNode.stepCost + 1
            newNode.childIndexes = childIndex
            newNode.index = childIndex
            newNode.camerasState = list(currentNode.camerasState)
            newNode.camerasState[childIndex] = False
            newNode.expand()
            nodesQueueByFScore.put(newNode,-newNode.fScore*1000 - newNode.stepCost)

