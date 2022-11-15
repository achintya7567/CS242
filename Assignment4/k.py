import sys

coins_available= [1, 5, 10, 20, 25, 50]

n=len(coins_available)

def Min_Coins(x):
    coins_required= [0 for i in range(x + 1)]
    coins_required[0]=0
    coins=[[]]

    for i in range(1, x + 1):
        coins_required[i] = x
    y=0
    for i in range(1, x + 1):
        l=[]
        k=0
        for j in range(n):
            if(coins_available[j]<=i):
                y=coins_required[i-coins_available[j]]
                if(y+1<coins_required[i]):
                    coins_required[i]=y+1;
                    k=coins_available[j]
        
        l.extend(coins[i-k])
        l.append(k)
        coins.append(l)


    if coins_required[x] == sys.maxsize:
         print(-1)
    else:  
        print("coins required=")
        print(coins_required[x])
        print(coins[x])
        

Min_Coins(100)
