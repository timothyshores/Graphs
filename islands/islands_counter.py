class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def island_counter(matrix):
    # create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    island_count = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if not visited
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    # Run some DFT and mark each as visited
                    dft(x, y, matrix, visited)

                    island_count += 1

    return island_count


def dft(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))

    while s.size() > 0:
        v = s.pop()
        x = v[0]
        y = v[1]

        if not visited[y][x]:
            # mark as visited
            visited[y][x] = True

            for neighbor in get_neighbors((x, y), matrix):
                s.push(neighbor)

    return visited


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]

    neighbors = []

    # North
    if y > 0 and graph_matrix[y-1][x] == 1:
        neighbors.append((x, y-1))

    # South
    if y < len(graph_matrix) - 1 and graph_matrix[y+1][x] == 1:
        neighbors.append((x, y + 1))

    # East
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))

    # West
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))

    return neighbors


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


print(island_counter(islands))


islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))
