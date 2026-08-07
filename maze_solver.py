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
    if not maze.solver_valid_position(start["x"], start["y"]) or not maze.solver_valid_position(goal["x"], goal["y"]):
        raise Exception("Start or Goal inside wall")
    

    stack.push([start["x"], start["y"]])
    maze.solver_visit(start["x"], start["y"])
    goal = [goal["x"], goal["y"]]
    while not stack.isEmpty():
        current = dict()
        current["x"], current["y"] = stack.peek()

        #9 is the path
        if [current["x"], current["y"]] == goal:
            print("Path Found, the stack has the route")
            path = []
            for z in range(0, stack.size()):
                x1, y1 = stack.pop()
                path.append([x1, y1])
            return path

        if maze.solver_valid_position(current["x"]+1, current["y"]):
            stack.push([current["x"]+1, current["y"]])
            maze.solver_visit(current["x"]+1, current["y"])

        elif maze.solver_valid_position(current["x"]-1, current["y"]):
            stack.push([current["x"]-1, current["y"]])
            maze.solver_visit(current["x"]-1, current["y"])

        elif maze.solver_valid_position(current["x"], current["y"]+1):
            stack.push([current["x"], current["y"]+1])
            maze.solver_visit(current["x"], current["y"]+1)

        elif maze.solver_valid_position(current["x"], current["y"]-1):
            stack.push([current["x"], current["y"]-1])
            maze.solver_visit(current["x"], current["y"]-1)

        else:
            stack.pop()

    return "No path exists"
        