from tkinter import *
import time
from maze import create_maze
from maze_solver import solve_maze
from map import Map

class Game():
    def __init__(self, dim, size = 10):

        """
        Self.root is the tkinter object in which everything else happens
        Self.canvas is the canvas widget inside self.root, on which the maze is drawn
        Self.dim is the dimensions of the maze, but due to some interestinf code, it is inaccurate
        The real dimensions are 2*dim+1. This will be fixed later.
        """

        self.root = Tk()
        self.size = size
        self.canvas = Canvas(self.root, width = int((2*dim+1)*size), height = int((2*dim+1)*size), bg="white")
        self.dim = dim
        self.canvas.pack()
        self.player_location = {"x":1, "y":1}


        self.root.bind("<r>", self.reload)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Left>", self.move_left)

    def move_up(self, event):
        print("Up")
        if self.player_location["y"] > 0 and not self.maze.game_check(self.player_location["x"], self.player_location["y"]-1, 1):
            self.canvas.move(self.player, 0, -self.size)
            self.player_location["y"] -= 1


    def move_down(self, event):
        print("Down")
        if self.player_location["y"] < self.dim*2 and not self.maze.game_check(self.player_location["x"], self.player_location["y"]+1, 1):
            self.canvas.move(self.player, 0, self.size)
            self.player_location["y"] += 1


    def move_right(self, event):
        print("Right")
        if self.player_location["x"] < self.dim*2 and not self.maze.game_check(self.player_location["x"]+1, self.player_location["y"], 1):
            self.canvas.move(self.player, self.size, 0)
            self.player_location["x"] += 1
            self.check_goal()

    def move_left(self, event):
        print("Left")
        if self.player_location["x"] > 0 and not self.maze.game_check(self.player_location["x"]-1, self.player_location["y"], 1):
            self.canvas.move(self.player, -self.size, 0)
            self.player_location["x"] -= 1

    def check_goal(self):
        if self.player_location["x"] == self.dim*2+1:
            self.root.destroy()
    def place_square(self, x, y, colour):
        """
        This methods places a square on the canvas at the designated x and y coordinates 
        with the square being the colour indicated
        The use of self.size is to change the size of the maze
        """
        square = self.canvas.create_rectangle(x*self.size, y*self.size, x*self.size+self.size, y*self.size+self.size, fill=colour, outline=colour)
        self.canvas.pack()
        return square

    def generate_maze(self):
        """
        This method generates a maze, with the dimensions given when the class is created.
        """
        self.maze = Map(create_maze(self.dim))
        return self.maze

    def generate_path(self):
        """
        This method generates a path through the maze at self.maze
        """
        self.path = solve_maze(self.maze.maze, self.dim)
        return self.path

    def draw_maze(self):
        """
        This method draws a maze, using the numbers to decide what colour each square should be, 
        because it iterates through a 2D list
        """
        for x in range(0, len(self.maze.maze)):
            for y in range(0, len(self.maze.maze[x])):
                if self.maze.game_check(x, y, 1):
                    self.place_square(x, y, "red")
                    self.canvas.create_text(x*20+10, y*20+10, text = 1, fill = "black")
                if self.maze.game_check(x, y, 0) or self.maze.game_check(x, y, 7):
                    self.place_square(x, y, "white")
                    self.canvas.create_text(x*20+10, y*20+10, text = 0, fill = "black")

    def draw_path(self):
        """
        This method draws a path of blue squares using coordinated from a list.
        """


        for coords in self.path:
            self.place_square(coords[0], coords[1], "blue")


    def reload(self, event):
        self.generate_maze()
        self.generate_path()
        self.draw_maze()
        #self.draw_path()
        self.player = self.place_square(self.player_location["x"], self.player_location["y"], "black")
        main.root.mainloop()


main = Game(10, 20)
main.reload(0)