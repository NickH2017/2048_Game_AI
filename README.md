# 2048 Game AI Program
The 2048 Game with an Expectimax AI algorithm
By Josue Perez and Nicolas Hernandez

## Introduction

For the final project we decided to recreate the popular computer game 4x4grid puzzle "2048" by implementing an expectimax algorithm ai to play it. 

### How does it play?

The game start with an 4x4 grid with two random key assign to a value between 2 or 4. The player must combine key tiles that are of the same values until the value 2048 has reach in the grid. To combine tiles the player much choose four action to move the grid. Those four action are up, down, left and right. Each action the player chooses will move all grid value that are not the "0" key tile to the designated direction by the player. The tile will move until it has reach the boundary of the grid or reach alongside a different value tile that is not zero. After the action is perform a random "0" tile on the grid would change from either a "2" or "4" tile.

Example:

## Getting Started

The following files should be in your working directory

```bash
main_driver.py
game.py
Expectimax.py
GUI.py (Optional)
```

To begin, compile and run main_driver.py 

In order to play this game you must have python 3.9 or 3.8 intall in your computer. Furthermore, you must also have pygame already set up and install in your computer. If you don't have these options, you can use the terminal option prompt from the user after running main_driver.py


## Usage

main_driver.py will prompt the user what to do. The program will also be input validating to allow for proper run.

If using the optional GUI.py, The bestway to test is to run GUI.py on it's own and comment out lines 224-225 to see the visual run of the AI.


### Goal
The main objective for this project was to implement an expectimax AI algorithm for the "2049"
puzzle to visualize how it solve 





