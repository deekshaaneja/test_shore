import queue
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.listOfAdjacentNodes = []
    
    def getId(self):
        return self.id
    
    def addFriend(self, friend):
        typeOfFriend = type(friend).__name__
        if typeOfFriend == 'User':
            self.listOfAdjacentNodes.append(friend)
            friend.listOfAdjacentNodes.append(self)
        else:
            print("adding a friend exception")
    
    def getFriends(self):
        return self.listOfAdjacentNodes

class PathNode:
    # user = None
    # previousNode = None
    def __init__(self, person, path):
        self.user = person
        self.previousNode = path
    
    def getPerson(self):
        return self.user
    
    def collapse(self):
        listOfUsers = []
        listOfUsers.append(self.user.getId())
        node = self.previousNode
        while node is not None:
            listOfUsers.append(node.user.getId())
            node = node.previousNode
        return listOfUsers

class BFSData:

    def __init__(self, user):
        path = PathNode(user, None)
        self.toVisit = queue.Queue()
        self.visited = {}
        self.toVisit.put(path)
        self.visited[user.getId()] = path
    
    def isFinished(self):
        return self.toVisit.qsize()
    
    def getVisited(self):
        return self.visited

    
def searchLevel(primary, secondary):
    count = primary.toVisit.qsize()
    for i in range(count):
        node = primary.toVisit.get()
        userId = node.getPerson().getId()
        user = node.getPerson()

        if userId in secondary.visited:
            return node.getPerson()
        
        # Add freinds to queue
        friends = user.getFriends()

        for friend in friends:
            if friend.getId() not in primary.visited:
                newPathNode = PathNode(friend, node)
                primary.toVisit.put(newPathNode)
                primary.visited[friend.getId()] = newPathNode
    return None

def mergePath(bfsdata1, bfsdata2, person):
    primaryVisitedList = bfsdata1.getVisited()
    secondaryVisitedList = bfsdata2.getVisited()
    personId = person.getId()
    primaryUserList = primaryVisitedList[personId].collapse()
    secondaryUserList = secondaryVisitedList[personId].collapse()
    return primaryUserList[::-1] + secondaryUserList[1:]

# userArr[0].addFriend(userArr[100])

def getPath(user1, user2):
    sourceData = BFSData(user1)
    destinationData = BFSData(user2)

    while sourceData.isFinished() > 0 and destinationData.isFinished() > 0:
        # search from source
        collision = searchLevel(sourceData, destinationData)
        if collision is not None:
            return mergePath(sourceData, destinationData, collision)
            # print("finally match found on primary")

        collision = searchLevel(destinationData, sourceData)
        if collision is not None:
            return mergePath(sourceData, destinationData, collision)
            # print("finally match found on secondary")


        


    












