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

### List of steps: (Mentioned in comments in more detail)

1. Form a dp array with the worst case scenario
2. cat function opens the file from which file names are read line by line and then copied to the destination folder with changed extension '.bak' (from any extension, not just txt as shown by 'backup3.html')
3. Outputs are shown according to the progress of the program.

## Question 2: Random string generator using Perl

### Submitted files:

-   Code file: 'Assignment2.pl'
-   Sample file that contains alphabet string to be used (named "input_characters.txt")

### How to run:

1. Go to the "input_characters.txt" file and input the string you wish to use.
2. Open a Unix based terminal and change to the folder containing the Assignment2.pl script.
3. Run the command "perl Assignment2.pl"
4. It takes 2 inputs from the user.

-   First, a count of maximum same letters in a substring.
-   Second, length of string to be outputted.

It then returns the randomly generated string or returns if the string cannot be generated in special cases of count and input file value.

### List of steps: (Mentioned in comments in more detail)

1. Opened the file for taking input alphabet string.
2. Taken input of length and count from the user and run validity checks for special cases.
3. The loop runs until the length of generated string is equal to the length input by user (as code inside the loop prevents it from being greater).
4. If condition inside loop also prevents from substring length being greater than count.
5. After all the checks, the string is updated.
