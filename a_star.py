import heapq
import geometry
import copy
import time

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
        self.index = 0
        self.cameras = []
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.fScore == other.fScore #and self.stepCost == self.stepCost
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
           # if (self.fScore == other.fScore):
               # return self.stepCost < other.stepCost
            return self.fScore< other.fScore
    def expand(self,gallery_polygon):
        (self.childIndexes,self.hScore) = geometry.getIndexOfCamerasToTurnOff(self.cameras, gallery_polygon, self.index)
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
        #print("FScore {} StepCost {} HScore {}".format(currentNode.fScore,currentNode.stepCost,currentNode.hScore))
        if currentNode.hScore == 0:
            return currentNode

        for (i,childIndex) in enumerate(currentNode.childIndexes):

            newNode = node()
            newNode.stepCost = currentNode.stepCost + 1
            newNode.childIndexes = childIndex
            newNode.cameras = copy.deepcopy(currentNode.cameras)

            newNode.expand(gallery_polygon)
            newNode.disableCamera(childIndex)


            nodesQueueByFScore.put(newNode,-newNode.fScore)

