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
        self.cameras = []
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.fScore == other.fScore
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.fScore< other.fScore
    def expand(self):
        self.childIndexes = geometry.getIndexOfCamerasToTurnOff(self.cameras)
        self.hScore =  len(self.childIndexes)
        self.fScore = self.stepCost + self.hScore
    def disableCamera(self,indexToDisable):
        self.cameras[indexToDisable].disableCamera()


def aStar(cameras):
    nodes=[]
    node1 = node()
    node2 = node()
    node1.fScore = 10
    node2.fScore = 3
    heapq.heappush(nodes, (1, node1))
    heapq.heappush(nodes, (2, node2))
    print(heapq.heappop(nodes)[1].fScore)
    root = node()
    root.cameras = cameras
    root.expand()
    s = node()
    s.fScore = 3

    nodesQueueByFScore = PriorityQueue()
    nodesQueueByFScore.put(root,-root.fScore)
    nodesQueueByFScore.put(s,-s.fScore)
    while not nodesQueueByFScore.empty():
        currentNode = nodesQueueByFScore.get()
        if currentNode.hScore == 0:
            break
        print(currentNode.childIndexes)
        for (i,childIndex) in enumerate(currentNode.childIndexes):
            newNode = node()
            newNode.stepCost = currentNode.stepCost + 1
            newNode.cameras = currentNode.cameras
            newNode.disableCamera(childIndex)
            newNode.expand()
            nodesQueueByFScore.put(newNode,-newNode.fScore)
