# Blocks World

## Problem Description

The blocks world is one of the most famous planning domains in artificial intelligence. The algorithm is similar to a set of wooden blocks of various shapes and colors sitting on a table. The goal is to build one or more vertical stacks of blocks. Only one block may be moved at a time: it may either be placed on the table or placed atop another block. Because of this, any blocks that are, at a given time, under another block cannot be moved. Moreover, some kinds of blocks cannot have other blocks stacked on top of them.

The simplicity of this toy world lends itself readily to classical symbolic artificial intelligence approaches, in which the world is modeled as a set of abstract symbols which may be reasoned about.

## About this project

It is a Blocks World puzzle game solver, with different kinds of algorithms. This project is created as an assignment of Artificial Inteligence university course.

## Usage

```
python main.py <search_method> <input_file> <output_file>
```

## Input File Format (.ini)

```
[START] # starting state
size=3,3  # grid size
a=0,2 # starting state of block a
b=1,2 # starting state of block b
agent=2,2 # starting state of agent

[GOAL]
a=1,1 # goal state of block a
b=1,2 # goal state of block b
```

## Output File Format (.txt)
```
a ('0, 2')
b ('1, 2')
----------
Nodes expanded: 1
----------
a ('0, 2')
b ('1, 2')
----------
Nodes expanded: 2
  .
  .
  .
----------
a ('1, 1')
b ('1, 2')
----------
Nodes expanded: 242
----------
--- Execution time (seconds): 0.006296873092651367 ---
```

## Solving methods

* A* Search Algorithm (astar)
* Best First Search Algorithm (best)
* readth First Search Algorithm (breadth)
* Depth First Search Algorithm (depth)
