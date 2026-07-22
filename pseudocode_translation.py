from stack import Stack
from colorama import Fore
import time
def valid(x, y, v):
    try:
        if v[x][y] == 0 and x >= 0 and y >= 0:
            return True
        return False
    except IndexError:
        return False

def solve_maze(start_x, start_y, goal_x, goal_y, visited = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                            [7, 0, 7, 7, 7, 7, 7, 7, 7, 0], 
                                            [7, 7, 7, 0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                            [7, 7, 7, 0, 7, 7, 7, 7, 7, 7],
                                            [0, 0, 7, 0, 7, 0, 0, 0, 0, 0], 
                                            [0, 0, 7, 0, 7, 0, 7, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]):
    stack = Stack()
    if not valid(start_x, start_y, visited) or not valid(goal_x, goal_y, visited):
        raise Exception("Start or Goal inside wall")
    

    stack.push([start_x, start_y])
    visited[start_x][start_y] = 1
    Goal = [goal_x, goal_y]
    while not stack.isEmpty():
        [current_x, current_y] = stack.peek()

        if [current_x, current_y] == Goal:
            print("Path Found, the stack has the route")


        if valid(current_x+1, current_y, visited):
            stack.push([current_x+1, current_y])
            visited[current_x+1][current_y] = 1

        elif valid(current_x-1, current_y, visited):
            stack.push([current_x-1, current_y])
            visited[current_x-1][current_y] = 1

        elif valid(current_x, current_y+1, visited):
            stack.push([current_x, current_y+1])
            visited[current_x][current_y+1] = 1

        elif valid(current_x, current_y-1, visited):
            stack.push([current_x, current_y-1])
            visited[current_x][current_y-1] = 1

        else:
            stack.pop()

    return "No path exists"
        
print(solve_maze(0, 0, 3, 0))