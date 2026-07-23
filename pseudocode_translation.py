from stack import Stack
from colorama import Fore
import time

#This is the map the maze solver function will use
MAP =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [7, 0, 7, 7, 7, 7, 7, 7, 7, 0], 
        [7, 7, 7, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [7, 7, 7, 0, 7, 7, 7, 7, 7, 7],
        [0, 0, 7, 0, 7, 0, 0, 0, 0, 0], 
        [0, 0, 7, 0, 7, 0, 7, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#x, y are x and y coordinates, v is the visited list(the big map grid 2d list).
def validate_position(x:int, y:int, v:list) -> bool:
    try:
        if v[x][y] == 0 and x >= 0 and y >= 0:
            return True
        return False
    except IndexError:
        return False
#returns a bool


#start x and y are the starting position, goalx and y are the ending indicies, visited is the maze it is solving
def solve_maze(start_x:int, start_y:int, goal_x:int, goal_y:int, visited:list = MAP):
    stack = Stack()
    if not validate_position(start_x, start_y, visited) or not validate_position(goal_x, goal_y, visited):
        raise Exception("Start or Goal inside wall")
    

    stack.push([start_x, start_y])
    visited[start_x][start_y] = 1
    goal = [goal_x, goal_y]
    while not stack.isEmpty():
        [current_x, current_y] = stack.peek()

        if [current_x, current_y] == goal:
            print("Path Found, the stack has the route")
            for z in range(0, stack.size()):
                x1, y1 = stack.pop()
                visited[x1][y1] = 0

                for x in visited:
                    for y in x:
                        if y == 0:
                            print(Fore.BLACK+"0, ", end = "")
                        elif y == 1:
                            print(Fore.GREEN+"1, ", end = "")
                        elif y == 7:
                            print(Fore.RED+"7, ", end = "")
                    print("")
                print(Fore.WHITE+"")
                time.sleep(0.1)
            return "Path has been found"

        if validate_position(current_x+1, current_y, visited):
            stack.push([current_x+1, current_y])
            visited[current_x+1][current_y] = 1

        elif validate_position(current_x-1, current_y, visited):
            stack.push([current_x-1, current_y])
            visited[current_x-1][current_y] = 1

        elif validate_position(current_x, current_y+1, visited):
            stack.push([current_x, current_y+1])
            visited[current_x][current_y+1] = 1

        elif validate_position(current_x, current_y-1, visited):
            stack.push([current_x, current_y-1])
            visited[current_x][current_y-1] = 1

        else:
            stack.pop()

    return "No path exists"
        
print(solve_maze(0, 0, 3, 0))