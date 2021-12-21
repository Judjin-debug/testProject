# Project 0. Guess the number.

## Contents
[1. Project description](https://github.com/Judjin-debug/testProject/blob/master/README.md#Project-description)
[2. What case is solved?](https://github.com/Judjin-debug/testProject/blob/master/README.md#What-case-is-solved)
[3. Short information about data](https://github.com/Judjin-debug/testProject/blob/master/README.md#Short-information-about-data)
[4. Stages of project](https://github.com/Judjin-debug/testProject/blob/master/README.md#Stages-of-project)
[5. Result] (https://github.com/Judjin-debug/testProject/blob/master/README.md#Result)

### Project description
Guess the number with minimal tries

:arrow_up:[to contents](https://github.com/Judjin-debug/testProject/blob/master/README.md#Contents)

### What case is solved
It's necessary to write a program that guesses a number

**Conditions:**
— Computer guesses a number from 0 to 100, and it's necessary to guess it. Guessing means writing an algorithm that does it.
— Algorithm considers whether the random number was less than the one it should guess.

**Metrics:**
Results are estimated by the mean average of 1000 tries.

:arrow_up:[to contents](https://github.com/Judjin-debug/testProject/blob/master/README.md#Contents)

### Short information about data
main.py - main executable file that launches the function with optimized searching algorithm
game_v2.py - a module that contains two algorithms,- an optimized and unoptimized one,- and compares them using a function that finds the mean average and a time decorator
game.py - a file where you guess a number manually
game.ipynb - an attempt to import game_v2.py to a jupyter notebook
requirements.txt, environment.yaml - files that describe dependencies

:arrow_up:[to contents](https://github.com/Judjin-debug/testProject/blob/master/README.md#Contents)

### Stages of project
1. Creation of game.py
2. Creation of game_v2.py with unoptimized search
3. Creation of game.ipynb
4. Creation of a GitHub repository
5. Generation of requirements.txt, environment.yaml
6. Addition of an optimized algorithm in game_v2.py file

:arrow_up:[to contents](https://github.com/Judjin-debug/testProject/blob/master/README.md#Contents)

### Result
The average amount of search iterations went from 101 to 5, which is 20.2 times less tries
The working time went from ~0.2253060 seconds to ~0.0049872 seconds, which is ~45.1768527 times faster