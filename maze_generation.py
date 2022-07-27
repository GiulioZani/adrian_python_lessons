import random
from colorama import init, Fore
import ipdb


"""
Maze-generating algorithm in plain English:

1) Initialize a matrix of unvisited locations
2) Pick a location, mark it as a cell (empty part of the maze). Add the four surrounding locations to a list of walls and mark them as walls.
3) While the list of walls is not empty:
    Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
        a) Make the wall a passage and mark the unvisited cell as part of the maze
        b) Add the neighboring walls of the cell to the wall list.
        c) Remove that wall from the list

Later on we will make it more elegant by using OOP (object oriented programming).
"""
# type annotation/type hinting/type wispering
def create_maze(height:int, width:int, unvisited:str) -> list[list[str]]:
    maze = []
    for _ in range(height):
        line = []
        maze.append(line)
        for _ in range(width):
            line.append(unvisited)
    return maze

def print_maze(maze:list[list[str]]) -> None:
    result = ""
    for line in maze:
        result += " ".join(line)
        result += "\n"
    print(result)

def main():
    init()
    height = 20
    width = 20
    cell = Fore.WHITE + "c"
    unvisited = Fore.GREEN + "u"
    wall = Fore.RED + "w"
    maze = create_maze(height, width, unvisited)
    start_height = int(random.random()*height)
    start_width = int(random.random()*width)

    if start_height == 0:
        start_height += 1
    if start_height == height - 1:
        start_height -= 1
    if start_width == 0:
        start_width += 1
    if start_width == width - 1:
        start_width -= 1

    maze[start_height][start_width] = cell
    walls = [
        (start_height - 1, start_width), # UP
        (start_height + 1, start_width), # DOWN
        (start_height, start_width - 1),
        (start_height, start_width + 1)
    ]
    for wall_height, wall_width in walls:
        maze[wall_height][wall_width] = wall

    while len(walls) > 0:
        random_wall = random.choice(walls)
        # Do step 3

    print_maze(maze)


if __name__ == "__main__":
    main()
