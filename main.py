# importing the libraries needed to label points and color the output to the terminal
from enum import Enum
from termcolor import colored


# creating a class called maze so that we can iterate through the maze
class Maze:

    # constructor to set the start and end as well as store the maze in an array
    def __init__(self):
        self.start = None
        self.end = None
        self.array = []


# creating a tile class to label the tile as a path or wall
class Tile(Enum):
    WALL = 1
    PATH = 0


# function to create the maze object by reading a txt file
def createMaze():
    # opening the maze file for reading
    f = open("path to maze and name of txt file containing the maze", "r")

    # creating an instance of the maze class
    maze = Maze()

    # double for loop to read through the liens of the file and label them
    y = 0

    for line in f:
        tiles = []
        x = 0

        # labeling the start, end, paths, and walls depending on the character
        for char in line:
            if char == "#":
                tiles.append(Tile.WALL)

            elif char == " ":
                tiles.append(Tile.PATH)

            elif char == "S":
                maze.start = (x, y)
                tiles.append(Tile.PATH)

            elif char == "E":
                maze.end = (x, y)
                tiles.append(Tile.PATH)

            # incrementing varibales
            x += 1

        # appending the labeled tile to the maze objects array
        maze.array.append(tiles)
        y += 1

    # returning the maze objcect created
    return maze


# function to display the maze before and after the path was found
def displayMaze(maze, path=[]):
    # double for loop to iterate through the array in the maze object
    y = 0

    for tiles in maze.array:
        x = 0

        # printing the tiles of the maze based on the tile class, and labeling the path if one is given
        for tile in tiles:
            if (x, y) in path:
                print(colored("o", "blue"), end="")

            elif (x, y) == maze.start:
                print("S", end="")

            elif (x, y) == maze.end:
                print("E", end="")

            elif tile == Tile.WALL:
                print(colored("#", "yellow"), end='')

            elif tile == Tile.PATH:
                print(" ", end='')

            # incrementing varibales and printing a new line
            x += 1

        print()
        y += 1


# function to search the maze using the Breadth First Algorithm
def mazeBFS(maze, verbose=False):
    # creating lists to hold path frontier and explored tiles
    explored = []
    frontier = []

    # setting the start of the maze and adding it to the explored and frontier list
    start = maze.start
    explored.append(start)
    frontier.append([start])

    # check if verbose to print the moves
    if verbose:
        print("Coordinates being searched to reach the goal state using BFS: \n")

    # main loop to iterate through the frontier of tiles
    while len(frontier) > 0:
        # setting the current to the front of the frontier
        stack = frontier.pop(0)
        current = stack[-1]

        # checking if verbose to print the current coord the search is at
        if verbose:
            print("Current coordinate in the maze: ", current)

        # checking if we are at the solution or not and returning the path if so
        if current == maze.end:
            return stack

        # for loops to search the adjacent tiles
        for y in range(-1, 2):
            for x in range(-1, 2):
                x2 = current[0] + x
                y2 = current[1] + y
                tile = maze.array[y2][x2]

                # appending the adjacent tile to current if it isn't a wall and hasn't been visited already
                if tile == Tile.PATH and (x2, y2) not in explored and (x2, y2) != current:
                    new_stack = stack.copy()
                    new_stack.append((x2, y2))
                    frontier.append(new_stack)
                    explored.append((x2, y2))


# function to search the maze using the Depth First Algorithm
def mazeDFS(maze, verbose=False):
    # setting the start of the maze and adding it to the explored and frontier list
    explored = []
    frontier = []

    # setting the start of the maze and adding it to the explored and frontier list
    start = maze.start
    explored.append(start)
    frontier.append([start])

    # check if verbose to print the moves
    if verbose:
        print("Coordinates being searched to reach the goal state using DFS: \n")

    # main loop to iterate through the frontier of tiles
    while len(frontier) > 0:
        # setting the current to the front of the frontier
        stack = frontier.pop(0)
        current = stack[-1]

        # checking if verbose to print the current coord the search is at
        if verbose:
            print("Current coordinate in the maze: ", current)

        # checking if we are at the solution or not and returning the path if so
        if current == maze.end:
            return stack

        # for loops to search the adjacent tiles
        for y in range(-1, 2):
            for x in range(-1, 2):
                x2 = current[0] + x
                y2 = current[1] + y
                tile = maze.array[y2][x2]

                # appending the adjacent tile to current if it isn't a wall and hasn't been visited already
                if tile == Tile.PATH and (x2, y2) not in explored and (x2, y2) != current:
                    new_stack = stack.copy()
                    new_stack.append((x2, y2))
                    frontier.insert(0, new_stack)
                    explored.insert(0, (x2, y2))


# main function to display the maze, run the searches, and display the search results
def main():
    # creating a maze object from the txt file
    maze = createMaze()

    # displaying the maze before it is solved
    print("Maze before being solved by DFS and BFS: ")

    displayMaze(maze)

    # running BFS on the maze and then printing the path found
    # mazeBFS(maze, True) will run the algorithm in verbose mode
    bfspath = mazeBFS(maze)

    print("\nMaze solved using BFS ( dots are equivalent to the path ) : \n")

    displayMaze(maze, bfspath)

    # running DFS on the maze and then printing the path found
    # mazeDFS(maze, True) will run the algorithm in verbose mode
    dfspath = mazeDFS(maze)

    print("\nMaze solved using DFS ( dots are equivalent to the path ) : \n")

    displayMaze(maze, dfspath)


if __name__ == '__main__':
    main()
