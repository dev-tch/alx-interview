### project 0x08. Making Change
```
# Notes:
    # back tracking  will not with this type of algorithm : ( repetition + overflow recursion) 
    # ==> we will work with dynamic programming 
    # Example : if we  have  a coin 4 and will want the amount 7 using  coin 4 
    # ==> dp[7] = 1(one coin of four) + dp[(7 - 4)(remaining amount after substructing coin 4)]
    # we initialize an array wih default value ( maximum : INFINITY or  of (total + 1)
    # dp[0] = 0 ; to form 0 amount we need 0 coins 
    # formula : for each coin :  dp[amount] = 1(one coin) +  dp[amount - coin] 
    # amount in the intervall [1, total]
    # excution example
    # coins = [1, 3 , 4 , 5]
    # we look for amount 7
    # init dp with [0, 8 , 8 , 8 , 8 , 8 , 8,  8]
    # we test  each amount  against each coin
    # example amount 1 against coins
    # dp[0] = 0
    # dp[1] = min(dp[1] , dp[0] + 1) = min(dp[1], 1) ( we now  dp[1] = 8) =  1
    # dp[1] # invalid condition for coin 3 ( 1 - 3 <= 0)
    # dp[1] # invalid condition for coin 4 (1 - 4 <= 0)
    # dp[1] # invalid condition for coin 5 (1 - 5 <= 0)
    # from this iterartion we have (dp[1] = 1 )
    # like differents arithmetic progression for each coin 
    # suite coin1
    # u(0) = 0
    # u(n) = u(n - 1) + 1   n-1 > 0  
     # suite coin3
    # u(0) = 0
    # u(n) = u(n - 3) + 1  n-3 > 0
    # suite coin4
    # u(0) = 0
    # u(n) = u(n - 4) + 1   n-4 > 0
    # suite coin5
    # u(0) = 0
    # u(n) = u(n - 5) + 1   n-5 > 0
    # to find the best smallest value between to assign to Un we have to apply 
    # u(n) = mininum of (u(n - 1) + 1 , u(n - 3) + 1 ,  u(n - 4) + 1, u(n - 5) + 1 ) againt un ( wiich initized with most big value  let say INFINITY )

```
