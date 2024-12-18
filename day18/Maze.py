from collections import deque

class Maze:
    def __init__(self, maze_map):
        self.maze = maze_map
        self.width = len(maze_map[0])
        self.height = len(maze_map)

    def find_shortest_path(self, start, end):
        queue = deque([(start, [])])  # Queue of (position, path) tuples
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == end:
                return path + [current]

            if current in visited:
                continue

            visited.add(current)
            for neighbor in self.get_neighbors(current):
                queue.append((neighbor, path + [current]))

        return None

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        if x > 0 and self.maze[y][x - 1] != "#":
            neighbors.append((x - 1, y))
        if x < self.width - 1 and self.maze[y][x + 1] != "#":
            neighbors.append((x + 1, y))
        if y > 0 and self.maze[y - 1][x] != "#":
            neighbors.append((x, y - 1))
        if y < self.height - 1 and self.maze[y + 1][x] != "#":
            neighbors.append((x, y + 1))
        return neighbors