def max_profit(prices):
    max_profit = 0
    length = len(prices)
    for i in range(length - 1):
        profit = prices[i + 1] - prices[i]
        if profit > max_profit:
            max_profit = profit
    return max_profit

prices= [50,20,70,90,30,0]
print("Possible max profit: ",max_profit(prices))