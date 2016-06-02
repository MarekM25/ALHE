import heapq
import geometry
import copy

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
    def expand(self,gallery_polygon):
        self.childIndexes = geometry.getIndexOfCamerasToTurnOff(self.cameras, gallery_polygon)
        self.hScore =  len(self.childIndexes)
        self.fScore = self.stepCost + self.hScore
    def disableCamera(self,indexToDisable):
        self.cameras[indexToDisable].disableCamera()


def aStar(cameras, gallery_polygon):
    root = node()
    root.cameras = cameras
    root.expand(gallery_polygon)
    nodesQueueByFScore = PriorityQueue()
    nodesQueueByFScore.put(root,-root.fScore)

    while not nodesQueueByFScore.empty():
        currentNode = nodesQueueByFScore.get()
        if currentNode.hScore == 0:
            return currentNode
        for (i,childIndex) in enumerate(currentNode.childIndexes):
            newNode = node()
            newNode.stepCost = currentNode.stepCost + 1
            newNode.cameras = copy.deepcopy(currentNode.cameras)
            newNode.disableCamera(childIndex)
            newNode.expand(gallery_polygon)
            nodesQueueByFScore.put(newNode,-newNode.fScore)
