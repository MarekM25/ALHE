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
    def expand(self):
        self.childIndexes = geometry.getIndexOfCamerasToTurnOff(self.cameras)
        self.hScore =  len(self.childIndexes)
        self.fScore = self.stepCost + self.hScore
    def disableCamera(self,indexToDisable):
        self.cameras[indexToDisable].disableCamera()


def aStar(cameras):
    root = node()
    root.cameras = cameras
    root.expand()
    nodesQueueByFScore = PriorityQueue()
    nodesQueueByFScore.put(root,-root.fScore)

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
