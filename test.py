from GetShortestPath import User, getPath
import time

userArr = []
lastUser = None

val = 10000000

for i in range(1000):
    name = "Ankit" + str(i)
    user = User(name, i)
    for k in range(100):
        new_name = "Friend" + "-" + str(i) + "-" + str(k)
        new_user = User(new_name, val)
        val += 1
        user.addFriend(new_user)

    if lastUser is not None:
        lastUser.addFriend(user)
        
    userArr.append(user)
    lastUser = user

# userArr[0].addFriend(userArr[100])

print("graph plotted")
time_start = int(time.time() * 1000)
print(getPath(userArr[0], userArr[101]))
time_end = int(time.time() * 1000)
print("graph plotted", time_end-time_start)


