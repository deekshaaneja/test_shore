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
    
    # def collapse(self, startWithRoot):
    #     path = list()
    #     node = self
    #     # while (node != None):

class BFSData:

    def __init__(self, user):
        path = PathNode(user, None)
        self.toVisit = queue.Queue()
        self.visited = {}
        self.toVisit.put(path)
        self.visited[user.getId()] = path
    
    def isFinished(self):
        return self.toVisit.qsize()

    
def searchLevel(peopleMap, primary, secondary):
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

userA = User("Ankit1", 1)
userB = User("Ankit2", 2)
userC = User("Ankit3", 3)
userD = User("Ankit4", 4)

userA.addFriend(userB)
userB.addFriend(userC)
userC.addFriend(userD)


sourceData = BFSData(userA)
destinationData = BFSData(userD)

while sourceData.isFinished() > 0 and destinationData.isFinished() > 0:
    # search from source
    peopleMap = {}
    collision = searchLevel(peopleMap, sourceData, destinationData)
    if collision is not None:
        print("finally match found on primary")
    collision = searchLevel(peopleMap, destinationData, sourceData)

    if collision is not None:
        print("finally match found on secondary")


        


    












