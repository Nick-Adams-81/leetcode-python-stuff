def max_profit(prices: list[int]) -> int:
    max_profit = 0
    min_buy = prices[0]

    for sell in prices:
        max_profit = max(max_profit, sell - min_buy)
        min_buy = min(min_buy, sell)
    return max_profit

prices = [10,1,5,6,7,1]
print(max_profit(prices))