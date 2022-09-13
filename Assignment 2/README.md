# README for Assignment 2:

### By: Achintya Gupta, Roll no.: 210101005

## Question 1: Backup Files using bash script

### Submitted files:

-   Code file: 'backup.scr'
-   Sample file that contains file names to be backued up (named "filename.txt")
-   'destination' directory with sample backup files formed during my run. The directory can be deleted, modified etc.
-   3 sample files that have been backed up namely:

1. backup1.txt
2. backup2.txt
3. backup3.html

### How to run:

1. Open a Unix based terminal and change to the folder containing the backup.scr script.
2. Run the command "bash backup.scr [ file name ] [ directory name ]" (or with any number of arguments)

#### Note: It is assumed that all the file names in the input file exist.

All the files named in the input file name are backed up.

### List of steps: (Mentioned in comments in more detail)

1. If else statements check the validity of the arguments and control the programme accordingly to check if the argument list is correct or not.
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
