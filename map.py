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
    def __init__(self, maze:list = MAP):
        self.maze = maze
        self.visited = maze

    def solver_visit(self, x:int, y:int, marker:int = 7):
        self.visited[y][x] = marker

    def solver_valid_position(self, x:int, y:int) -> bool:
            try:
                if self.visited[y][x] == 0 and x >= 0 and y >= 0:
                    return True
                return False
            except IndexError:
                return False

    def game_check(self, x:int, y:int, num:int) -> bool:
         if self.maze[y][x] == num:
              return True
         else:
              return False