# Assignment 3

#### By Achintya Gupta, Roll no.:210101005

### Question 1: Josephus problem

#### How to run:

-   Make sure you have python3 installed in the system
-   Open a terminal and navigate to the folder where the file is stored
-   Type "python3 210101005_Assign03_Q1.py"

#### How it works:

-   A signle list with entries from 1 to n is formed.
-   Index 1 is assigned as initial shooter and k-th person is figured out (modulo number of alive people left) by adding k to the index.
-   The loop works until only 1 person is left alive.
-   All actions are printed.

#### Variable names:

-   All variable names are self-explanatory

### Question 2: 8 Piece Puzzle:

#### How to run:

-   Make sure you have python3 installed in the system
-   Open a terminal and navigate to the folder where the file is stored
-   Type "python3 210101005_Assign03_Q2.py"

#### How it works:

-   Method used: Heuristic
-   Cost function: (Average distance)\*(Number of incorrectly placed tiles)
-   Goes to all possible nearby states and chooses the one with minimum cost
-   Keeps track of visited states so it doesn't end up repeating states.
-   If it reaches a state where all other nearby states are visited, it randomly chooses any of them to move out of a loop.

#### Variable names:

-   Explained in comments
