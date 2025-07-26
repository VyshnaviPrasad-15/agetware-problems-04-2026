def find_minimum_loss(prices):
    n = len(prices)
    if n < 2:
        print("No valid loss possible!")
        return
    
    min_loss = float('inf')
    buy_year = -1
    sell_year = -1
    
    # Keep track of minimum price seen so far and its year
    for i in range(n):
        # Check all future years for a possible loss
        for j in range(i + 1, n):
            if prices[i] > prices[j]:  # Ensure loss (buy price > sell price)
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1
                    sell_year = j + 1
    
    if min_loss == float('inf'):
        print("No valid loss possible!")
    else:
        print(f"Buy in year {buy_year} and sell in year {sell_year} with a loss of {min_loss}.")

if __name__ == "__main__":
    n = int(input("Enter number of years: "))
    prices = []
    for i in range(n):
        price = int(input(f"Enter price for year {i+1}: "))
        prices.append(price)
    
    find_minimum_loss(prices)