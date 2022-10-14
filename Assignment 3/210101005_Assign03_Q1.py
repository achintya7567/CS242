#Taking required inputs from the user
n=int(input("Input n: "))
k=int(input("Input k: "))

#Initializing list with all people
members_alive=[]
for i in range(1,n+1):
    members_alive.append(i)

#Initializing starting position
shooter_index=1

#Loop runs till one person remains
while len(members_alive)>1:

    #Number associated with the person shooting in this round
    killer = members_alive[shooter_index-1]

    #The person who was shot in the given round
    killed_index = (shooter_index+k-1) % len(members_alive)
    killed_number = members_alive.pop(killed_index)

    #Printing required output
    print(killer, "has killed", killed_number)

    #Updating the new shooter as the person standing next to the previous person killed
    shooter_index = killed_index+1
    shooter_index = shooter_index % len(members_alive)
print(members_alive[0], "has survived")