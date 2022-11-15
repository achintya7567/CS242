# README for Assignment 4:

### By: Achintya Gupta, Roll no.: 210101005

### Submitted files:

-   Q1.py, Q2_page1.tex, Q2_page2.tex

## Question 1: Python programme to find the minimum coins required to make a certain amount

### How to run:

-   Make sure you have python3 installed in the system
-   Open a terminal and navigate to the folder where the file is stored
-   Type "python3 Q1.py"
-   Give input number without presence of any other type of character

#### Note: The programme works for sufficiently large input in quick time (upto 10^6) and for 10^7 in some time. It is advised to not run for larger inputs as it may take up too much memory and cause the system to hang.

### List of steps:

1. Form a dp array with the worst case scenario and initialize the base cases for 0 and all denominations given
2. To reach given amount, you must have taken one of the given denominations as the last coin and even if you remove that coin, it would be the minimum steps to reach the previous amount.
3. This inductively (and recursively) should give the best composition. This minimum number of steps is stored for each number less than or equal to n
4. Then to find the composition we can backtrack from the n-th index to the 0th index, and find which denomination came just before (it would have taken dp_list[ n ]-1 steps) and store it in a list
5. This list is printed using some python functions for clean representation.

## Question 2: Latex pages

### How to run:

1. Ensure you have latex and its packages installed to run Latex
2. Open a tex editor like Texmaker (offline) or Overleaf (online)

-   If texmaker not present, run on terminal: sudo apt-get install texmaker

3. Compile and make pdf of the code

Alternatively:

-   Run the command "pdflatex Q2_page1.tex" to form a pdf file of the tex and it can be then opened.
-   Similarly run "pdflatex Q2_page2.tex"

#### Note: Run the commands twice as the referencing does not work properly the first time due to problem of how latex works.

### List of environments used:

-   math mode (inline using $ maths $ or new line using $$ maths $$)
-   equation and equation\*
-   align\*
-   matrix, pmatrix, bmatrix

### List of packages:

-   amsmath for some required environments
-   hyperref for references and colouring the links

### Symbols used:

-   Standard physics and maths symbols used throughout the code with reference of standard latex documentation.
-   tag{} is used to tag the equations with a number at the end of the line
-   label{eq:1} is used to label the equations so they can be referenced later
-   \textrm is used to write text inside math mode without italicizing (cannot write maths inside this)
-   \mathrm used to write chemistry equations (does not italicize letters but you can write math)

#### Note: Page numbers not removed as it was not clear in the image if it was just cropped or actually absent.
