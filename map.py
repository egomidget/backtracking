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
    def __init__(self, maze:list = MAP, walls:list = [7]):
        self.maze = maze
        self.walls = walls or []
        self.visited = maze

    def visit(self, x:int, y:int, char:int = 1):
        self.visited[y][x] = char

    def valid_position(self, x:int, y:int) -> bool:
            try:
                if self.visited[y][x] == 0 and x >= 0 and y >= 0:
                    return True
                return False
            except IndexError:
                return False

