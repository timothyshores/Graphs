import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i}")  # debug function

        target_friendships = numUsers * avgFriendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            userID = random.randint(1, self.lastID)
            friendID = random.randint(1, self.lastID)
            if self.addFriendship(userID, friendID):
                total_friendships += 2
            else:
                collisions += 1

        print(f"Collisions: {collisions}")

        possible_friendships = []

        # Create friendships
        for UserID in self.users:
            for friendID in range(UserID + 1, self.lastID + 1):
                possible_friendships.append((UserID, friendID))

        random.shuffle(possible_friendships)

        for i in range(numUsers * avgFriendships // 2):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        qq = Queue()

        qq.enqueue([userID])

        while qq.size() > 0:
            path = qq.dequeue()
            v = path[-1]

            if v not in visited:
                visited[v] = path

                for neighbor in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    qq.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 50)
    print("Friendships")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("Connections")
    print(connections)
    print(f"User in extended social network: {len(connections) - 1}")

    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])

    print(
        f"Average length of social path: {total_social_paths//len(connections)}")
