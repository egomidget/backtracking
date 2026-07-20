from stack import Stack

def valid(x, y, v):
    try:
        if v[x][y] == 0:
            return True
        return False
    except IndexError:
        return False

def solve_maze(start_x, start_y):
    stack = Stack()
    visited = [[0, 0], 
               [0, 0]]
    if not valid(start_x, start_y, visited):
        raise IndexError
    

    stack.push([start_x, start_y])
    visited[start_x][start_y] = 1
    Goal = [1, 1]
    while not stack.isEmpty():
        [current_x, current_y] = stack.peek()
        visited[current_x][current_y] = 1
        if [current_x, current_y] == Goal:
            print("Path Found, the stack has the route")
            break

        if valid(current_x+1, current_y, visited):
            stack.push([current_x+1, current_y])
        elif valid(current_x-1, current_y, visited):
            stack.push([current_x-1, current_y])
        elif valid(current_x, current_y+1, visited):
            stack.push([current_x, current_y+1])
        elif valid(current_x, current_y-1, visited):
            stack.push([current_x, current_y-1])

        
solve_maze(0, 0)