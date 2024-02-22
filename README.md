## README
This Python code implements a visualization tool for three sorting algorithms: Insertion Sort, Bubble Sort, and Shell Sort using the Pygame library. The program allows users to interactively visualize how these sorting algorithms work on a randomly generated list of numbers.

## Installation and Setup
Ensure you have Python installed on your system. You can download it from python.org.
Install Pygame by running pip install pygame in your terminal or command prompt.

## Usage
Run the Python script sorting_visualizer.py.
Once the program is running, you will see a Pygame window with the sorting algorithms' visualization.

## Use the following controls:
R: Restart and generate a new random list.
Space: Start sorting the list using the selected algorithm.
A: Set the sorting order to ascending.
D: Set the sorting order to descending.
I: Select Insertion Sort algorithm.
B: Select Bubble Sort algorithm.
S: Select Shell Sort algorithm.

## Functionality
The program generates a random list of numbers within a specified range.
Users can select the sorting algorithm (Insertion Sort, Bubble Sort, Shell Sort) and the sorting order (ascending or descending).
Visualization displays the current state of the list during sorting.
The program supports dynamic resizing of the Pygame window according to the size of the list.

## Code Structure
The code is structured into several functions and a main loop controlled by Pygame events.
Each sorting algorithm (Insertion Sort, Bubble Sort, Shell Sort) is implemented as a generator function to allow visualization during sorting.
Pygame is used for creating the graphical interface and displaying the sorting process.

## Dependencies
-Python 3.x
-Pygame
