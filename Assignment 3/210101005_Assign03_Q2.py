import copy
import random
from math import floor


"""Taking Input of matrix in the form of 3 1*3 lists and 9 in place of empty space
Sample:
1 2 3
4 5 6
7 8 9
"""

matrix=[]
goal=[]

print("Input Starting Matrix")
for i in range(3):
    matrix.append([int(x) for x in input().split()])

print("Input Goal Matrix")
for i in range(3):
    goal.append([int(x) for x in input().split()])



print()
print("START OF OUTPUT")
print()
visited=[]
chosen=[]
visited.append(copy.deepcopy(matrix))
chosen.append(copy.deepcopy(matrix))
#Functions

#For finding element in the matrix
def findElement(x, arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j]==x:
                return [i,j]

#For printing all elements of an array
def printf(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    print()

#To check if the problem is solvable using inversion count
def solvable():
    linear_matrix=[]
    mat=copy.deepcopy(matrix)
    cnt=0
    for i in mat:
        for j in i:
            if(j!=9):
               linear_matrix.append(j) 
     
    for i in range(8):
        for j in range(i,8):
            if linear_matrix[j]<linear_matrix[i]:
                cnt+=1
    linear_matrix=[]
    for i in goal:
        for j in i:
            if(j!=9):
                linear_matrix.append(j) 
     
    for i in range(8):
        for j in range(i,8):
            if linear_matrix[j]<linear_matrix[i]:
                cnt+=1
    if(cnt%2==0):
        return True
    else:
        return False

#To find coordinates of the empty tile
def spaceX():
    return findElement(9, matrix)[0]
def spaceY():
    return findElement(9, matrix)[1]

#To move a tile into empty space, x is the numerical value of the tile being moved there
def shift(x):
    global matrix
    y=9
    findx=findElement(x, matrix)
    findy=findElement(y, matrix)
    matrix[findx[0]][findx[1]],matrix[findy[0]][findy[1]] = matrix[findy[0]][findy[1]], matrix[findx[0]][findx[1]]

#Defined a type of distance of a tile, increases readability
#Also easier to edit the function
def distance(x):
    return abs(findElement(x,matrix)[0]-findElement(x, goal)[0])+abs(findElement(x,matrix)[1]-findElement(x, goal)[1])
           
#Cost function that decided if we should go into a position or not
def cost():
    Cost =0
    if(isGoal()):
        return 0
    else:
        #Cost1 is sum of minimum number of moves to take the tile to its place if only that is moved
        Cost1=0
        for i in matrix:
            for j in i:
                Cost1+=distance(j)

        #Cost2 is the number of misplaced tiles
        Cost2=0
        for i in range(3):
            for j in range(3):
                if goal[i][j]!=matrix[i][j]:
                    Cost2+=1

        #Taking average distance per tile and multiply by number of misplaced tiles
        Cost=(Cost1/9)*2.5*Cost2
        
        return Cost
    
    
#Returns if goal configuration is reached
def isGoal():
    global matrix
    return matrix==goal

#Finding which configuration to be chosen
def chooseConfig():

    #Global allows us to to make changes in global variables, matrix and visited and not form local variables
    global matrix, visited
    copyMat=copy.deepcopy(matrix)
    cost_list=[]
    pref=0

    #possible_list contains the which of the 4 moves are possible
    possible_list=[]

    #First move, moving upper tile to space
    if spaceX()-1>=0:
        possible_list.append(1)
        shift(matrix[spaceX()-1][spaceY()])

        #To prevent going back to an older move
        if matrix not in chosen:
            cost_list.append(cost())
            pref=1
            visited.append(copy.deepcopy(matrix))
        
        #Reverting matrix to original
        matrix=copy.deepcopy(copyMat)

    #This is below to up move
    if spaceX()+1<3:
        possible_list.append(2)
        shift(matrix[spaceX()+1][spaceY()])
        cost2=cost()
        if matrix not in chosen:
            visited.append(copy.deepcopy(matrix))

            #This is the preferred move only if it's cost is lesser than all previous moves
            for i in cost_list:
                if cost2>i:
                    break
            else:
                pref=2
                cost_list.append(cost2)
        matrix=copy.deepcopy(copyMat)

    #This is left to right move, rest same as previous
    if spaceY()-1>=0:
        possible_list.append(3)
        shift(matrix[spaceX()][spaceY()-1])
        cost3=cost()
        if matrix not in chosen:
            visited.append(copy.deepcopy(matrix))
            
            for i in cost_list:
                if cost3>i:
                     break
            else:
                pref=3
                cost_list.append(cost3)
        matrix=copy.deepcopy(copyMat)

    #This is right to left move, rest same as previous
    if spaceY()+1<3:
        possible_list.append(4)
        shift(matrix[spaceX()][spaceY()+1])
        cost4=cost()
        if matrix not in chosen:
            visited.append(copy.deepcopy(matrix))
            for i in cost_list:
                if cost4>i:
                    break
            else:
                pref=4
                cost_list.append(cost4)
        matrix=copy.deepcopy(copyMat)

    #If all moves are already visited earlier, we randomly choose any of the moves possible
    if(pref==0):
        pref=random.choice(possible_list)

    #Make the final preferred move that changes the matrix
    if(pref==1):
        shift(matrix[spaceX()-1][spaceY()])
    elif(pref==2):
        shift(matrix[spaceX()+1][spaceY()])
    elif(pref==3):
        shift(matrix[spaceX()][spaceY()-1])
    elif(pref==4):
        shift(matrix[spaceX()][spaceY()+1])




#Main Driver Code 
count=0
if not solvable():
    print("Puzzle is not solvable")
else:
    prev_pref=0
    while not isGoal():
        chooseConfig()
        chosen.append(copy.deepcopy(matrix))
        count+=1
        if count>100:
            break
    if count<=100:
        for i in chosen:
            printf(i)
        print("Solved in", count, "moves")
    else:
        print()
        print("Reachable but the algorithm takes more than 100 moves") 
    print()