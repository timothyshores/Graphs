# will be searching for the longest valid path -- calls for DFS using a stack
class Stack():
    # initialize an empty list for the stack
    def __init__(self):
        self.stack = []
 
    # Add new elements to the end of the stack
    def push(self, value):
        self.stack.append(value)

    # Remove the last element from the stack 
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    # Return the number of elements in the stack
    def size(self):
        return len(self.stack)

# Return the earlist ancestor from a list of (parent, child) pairs of ancestors and a starting node
# If there are multiple earliest ancestors the function returns the smaller value
def earliest_ancestor(ancestors, starting_node):

    def get_parents(child):
        """
        returns array of parents (neighbors) of child (value)
        graph will be DIRECTIONAL -- we only want to consider ancestors, so
        we will only search upwards through the parental heritage, never searching downward
        """
        return [pair[0] for pair in ancestors if pair[1] == child]

    # return -1 if starting node has no parents
    if get_parents(starting_node) == []:
        return -1

    visited = set()
    s = Stack()
    s.push([starting_node])

    # ancestor path will keep track of longest running path
    ancestor_path = []

    # while Stack s is empty
    while s.size() > 0:
        # Set path to the last element in the stack
        path = s.pop()
        last_child = path[-1]
        parents = get_parents(last_child)
        if len(parents) == 0:
            # if end of tested path has no parents, the path becomes current ancestor path
            # but only if it's longer than the current a_path
            # in case of tie, the path with the lowest-value earliest ancestor wins
            if len(path) > len(ancestor_path) or (len(path) == len(ancestor_path) and path[-1] < ancestor_path[-1]):
                ancestor_path = path
        visited.add(last_child)
        for parent in parents:
            copy = path.copy()
            copy.append(parent)
            s.push(copy)

    return ancestor_path[-1]


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 1))
