import heapq

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

def getIndexOfElements():
    return [1,2,3]


def aStar():
    #initCircleAndTurnsOff()
    #circleAndTurnsOff =
    root = node()
    root.childIndexes = getIndexOfElements()
    root.hScore = len(root.childIndexes)
    root.fScore = root.stepCost + root.hScore
    nodesQueueByFScore = PriorityQueue()
    nodesQueueByFScore.put(root,root.fScore)



    while not nodesQueueByFScore.empty():
        currentNode = nodesQueueByFScore.get()
        if currentNode.hScore == 0:
            break
        for i in range(len(currentNode.childIndexes)):
            print(currentNode.childIndexes[i])