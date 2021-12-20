
MAZE SOLVER
(Python Project)

Name – SUBIR GHOSH 

Batch – H.J. Bhabha 

Table of contents – 
1. Introduction 
2. Python Files 
3. Key Features 
4. Language used 
5. Future aspect 
1. Introduction – 
The aim of this project is to build a python program that runs as a command-line tool. It should take the input and output file name as command-line arguments. Using the square matrix present in the input file it should generate a path to reach the end of the maze and put it in the output file. If the maze is unsolvable, it should return -1 as the only value in the output file. As with every maze certain paths are blocked and are marked in grey in the image below. 
2. Python files – 
I. creat_maze.py – This is the file which has to run on terminal to Generate maze 
Do install numpy before generating the maze
1.	It takes the input from the user In the Form N * N
2.	If you don't want to generate then you can edit Input.txt
Thus it will generate your maze
II. maze_solve.py – This file consists of all the functionalities, It takes the input matrix , By using BFS finds all the path, By using dijkastra find the shortest path. It gives the output in the form of matrix in the output file output.txt 
III. input.txt – In this file generated input will stored in form of matrix Where 0 is all the blocked paths and 1 is all the paths that you can go to. 
IV. output.txt –This file will generate answer. if the answer is there then there will be Matrix if not then the Answer will be -1. 
3. Key Features – 
The system is having – 
a). One input file for take input 
b). One input file for display result 
This is done in two processes 
1. By providing with an interactive command prompt based shell where commands can be typed in. 
2. creat_maze.py file generate maze. 
3. maze_solve.py file search the shortest path to reach destination. If it found then it prints that path otherwise returns -1.
4. Language Used – 
The programming language is used python 3.9.9
5. Future aspect – 
I will add front end to this code. 
Also use tkinter to make a GUI program.	

