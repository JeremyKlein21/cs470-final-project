# 470 Final Project

This program solves mazes that were originally images using a Breadth First and Depth First Search

In order for the code to read the maze it must first be converted to an ASCII code maze consisting of `#` for the walls and spaces for the paths

Once the maze has been converted you can simply change the name of the text file in the code to what text file you want to run

~~~bash 
26 f = open("path to maze txt file and name of file", "r")

Example:
f = open("asciiMazes/maze.txt", "r")
    - asciiMazes is the folder where the txt file is located 
    - maze.txt is the name of the txt file containing the ASCII code
~~~

Each maze also has the option to be run with a verbose mode on when calling the search algorithm which will print the coordinates at each step of the algorithm. 

To run the algorithms so they display the current coordinates being searched:
~~~ bash
196 bfspath = mazeBFS( maze object, True )

203 dfspath = mazeDFS( maze object, True )
~~~

