#create a virual environment
> virtualenv socialgraph
> source socialgraph/bin/activate
> pip install -r requiremets.txt
> python test.py

# we are creating a graph with 100,000 nodes and searching for the connection between user 1 anduser 2
#the code in test.py is self explantory on how to add users and add friends
# We are doing a BFS from the source and from the destination and merging the paths when there is a collision.
# let's say that each user has k connections and the distance between them is l, then the time complexity would be O(k^(l/2)) + O(k^(l/2)) = O(k^(l/2))
# if we had done one bfs then the complexity would have been O(k^(l))
 


