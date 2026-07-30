from maze_solver import solve_maze
from maze import create_maze
import keyboard
from colorama import Fore
import os





#Update will delete the previous list and print a new one
def update(list):
    os.system("clear")
    for x in list:
        for y in x:
            if y == 0:
                print(Fore.CYAN+"0  ", end = "")
        print("")

def main():
    while True:
        x, y = 0, 0
        if keyboard.is_pressed("w"):
            while keyboard.is_pressed("w"):
                pass
            if y > 0:
                y -= 1
        if keyboard.is_pressed("s"):
            while keyboard.is_pressed("s"):
                pass
            if y < 1:
                y += 1
        if keyboard.is_pressed("a"):
            while keyboard.is_pressed("a"):
                pass
            if x < 1:
                x += 1
        if keyboard.is_pressed("d"):
            while keyboard.is_pressed("d"):
                pass
            if x > 0:
                x -= 1
        list = [[0, 0], [0, 0]]
        list[y][x] = 1
        update(list)

main()

