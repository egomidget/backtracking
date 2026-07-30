from stack import Stack
from map import Map
#This is the map the maze solver function will use



def solve_maze(MAP, dim) -> str:
    """
        start x and y are the starting position, goalx and y are the ending indicies, visited is the maze it is solving
    """

    stack = Stack()
    start = {"x":0, "y":1}
    goal = {"x":2*dim, "y":2*dim-1}

    maze = Map(MAP)
    if not maze.valid_position(start["x"], start["y"]) or not maze.valid_position(goal["x"], goal["y"]):
        raise Exception("Start or Goal inside wall")
    

    stack.push([start["x"], start["y"]])
    maze.visit(start["x"], start["y"])
    goal = [goal["x"], goal["y"]]
    while not stack.isEmpty():
        current = dict()
        current["x"], current["y"] = stack.peek()

        if [current["x"], current["y"]] == goal:
            print("Path Found, the stack has the route")
            for z in range(0, stack.size()):
                x1, y1 = stack.pop()
                maze.visit(x1, y1, 9)
            return "Path was found"

        if maze.valid_position(current["x"]+1, current["y"]):
            stack.push([current["x"]+1, current["y"]])
            maze.visit(current["x"]+1, current["y"])

        elif maze.valid_position(current["x"]-1, current["y"]):
            stack.push([current["x"]-1, current["y"]])
            maze.visit(current["x"]-1, current["y"])

        elif maze.valid_position(current["x"], current["y"]+1):
            stack.push([current["x"], current["y"]+1])
            maze.visit(current["x"], current["y"]+1)

        elif maze.valid_position(current["x"], current["y"]-1):
            stack.push([current["x"], current["y"]-1])
            maze.visit(current["x"], current["y"]-1)

        else:
            stack.pop()

    return "No path exists"
        