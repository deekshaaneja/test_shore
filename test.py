from GetShortestPath import User, getPath

userArr = []
lastUser = None
for i in range(10000):
    name = "Ankit" + str(i)
    user = User(name, i)
    if lastUser is not None:
        lastUser.addFriend(user)
    userArr.append(user)
    lastUser = user

print(getPath(userArr[0], userArr[10]))
