denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

# Greedy works because denomations are atleast 2 times greater than previous
# Ex: [1,5,6,9] for amount of 9 doesn't give optimal solution with greedy as denomations are not twice of previous


def findMinimumCoins(amount):
    
    # Time Complexity: O(N*M) - for every denomination n, runs m times dependent on i
    # Space Complexity: O(1), to return coin set will be O(N)
    
    # Calculate min coins in reverse order of denominations
    min_coins = 0
    remaining_amount = amount
    coin_set = []
    
    # Calculate min coins and coin set
    for coin in denominations[::-1]:
        if remaining_amount == 0:
            # If amount achieved
            break
        if remaining_amount == coin:
            # If amount will be achieved with 1 current coin
            remaining_amount -= coin 
            min_coins += 1
            coin_set.append((coin,1))
        elif remaining_amount > coin:
            i = 1
            # Can be infinite loop
            while(remaining_amount > 0):
                # Update i based on value that satisfies
                if ((remaining_amount - (coin * i)) == 0):
                    # If ra = 0, then optimal number of coins achieved
                    break
                elif ((remaining_amount - (coin * i)) < 0):
                    # If ra < 0, then optimal number of coins achieved can be achieved from previous number
                    i -= 1
                    break
                else:
                    # If ra > 0, then optimal number of coins achieved will be found in future
                    i += 1
            remaining_amount -= ( coin * i)
            min_coins += i
            coin_set.append((coin,min_coins))
    
    return min_coins
	
