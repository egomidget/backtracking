MAP =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 7, 0, 7, 7, 7, 7, 7, 7, 0], 
        [0, 7, 0, 0, 0, 0, 0, 0, 7, 7], 
        [0, 7, 0, 7, 7, 7, 7, 0, 0, 0], 
        [0, 7, 0, 7, 7, 7, 7, 7, 7, 7],
        [0, 7, 0, 7, 0, 0, 0, 0, 0, 0], 
        [0, 7, 0, 7, 0, 7, 0, 0, 0, 0], 
        [0, 7, 0, 7, 0, 7, 0, 0, 0, 0], 
        [0, 7, 0, 7, 0, 7, 0, 0, 0, 0], 
        [0, 7, 0, 0, 0, 0, 0, 0, 0, 0]]


class Map:
    def __init__(self, maze = MAP, walls = [7]):
        maze = self.maze
        walls = self.walls or []
        visited = self.maze

    def visit(self, x, y):
        self.visited[y,x] = 1

    def valid_position(self, x, y):

