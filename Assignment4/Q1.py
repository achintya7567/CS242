'''
Assignment 4, Q1
By: Achintya Gupta
Roll no: 210101005
'''


'''
To initialize the list to maximum possible value using list comprehension 
(It can't be more than using all 1 coins, i.e. i/1 coins)
This will later be reduced step by step using a dynamic programming (dp) strategy
'''


n=int(input("Enter the number: "))
denominations= [1,5,10,20,25,50]
dp_list=[i for i in range(n+1)]
dp_list[0]=0        #Base case

#All denominations take 1 step to reach, this is base condition on which our dp is built

for denom in denominations:
    if(denom<=n):
        dp_list[denom]=1

#Chooses best strategy to reach this amount, basically chooses the denomination by which we reached here in minimum steps
for val in range(1,n+1):
    for denomination in denominations:
        if val>=denomination:
            dp_list[val]=min(dp_list[val], dp_list[val-denomination]+1)



'''
composition variable stores the final composition of coins required.
iter is an iterator that is used to backtrack from n to 0.
It chooses the best denomination using a greedy approach on our dp array
'''


composition=[]  
iter=n
while iter!=0:
    for denom in denominations:
        if iter-denom>=0 and dp_list[iter-denom]==dp_list[iter]-1:
            composition.append(denom)
            iter=iter-denom


#String formatting used to print n-th element of the dp array which contains the minimum no. of coins required
print(f"Minimum required coins are {dp_list[n]}")

#.join function joins the elements of a string list (removes the brackets and commas)
# map function converted the integer composition array to a string array
print("The composition of numbers is:", ' '.join(map(str, composition)))

for i in denominations:
    print(f"Number of {i} coins: {composition.count(i)}")
