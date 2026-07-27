from stack import Stack
from map import Map
from colorama import Fore
import time
#This is the map the maze solver function will use
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



def solve_maze(start : dict = {"x": 0, "y": 0}, 
               goal : dict = {"x": 0, "y": 0}, 
               visited : list = MAP) -> str:
    """
        start x and y are the starting position, goalx and y are the ending indicies, visited is the maze it is solving
    """


    stack = Stack()
    maze = Map(MAP)
    if not maze.valid_position(start["x"], start["y"]) or not maze.valid_position(goal["x"], goal["y"]):
        raise Exception("Start or Goal inside wall")
    

    stack.push([start["x"], start["y"]])
    visited[start["x"]][start["y"]] = 1
    goal = [goal["x"], goal["y"]]
    while not stack.isEmpty():
        current = dict()
        current["x"], current["y"] = stack.peek()

        if [current["x"], current["y"]] == goal:
            print("Path Found, the stack has the route")
            for z in range(0, stack.size()):
                x1, y1 = stack.pop()
                maze.visit(x1, y1, 9)
            print("")
            print(Fore.GREEN+"Green is where the program explored")
            print(Fore.BLACK+"Grey is where the program did not explore")
            print(Fore.RED+"Red is where the walls are")
            print(Fore.CYAN+"Blue thows the path found, but this path may not be the shortest")
            print("")

            for x in maze.visited:
                for y in x:
                    if y == 0:
                        print(Fore.BLACK+"0, ", end = "")
                    elif y == 1:
                        print(Fore.GREEN+"1, ", end = "")
                    elif y == 7:
                        print(Fore.RED+"7, ", end = "")
                    elif y == 9:
                        print(Fore.CYAN+"9, ", end = "")
                print("")
            print(Fore.WHITE+"")
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
        
print(solve_maze({"x":0, "y": 0}, {"x":9, "y":7}))