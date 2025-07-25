def minimize_loss(prices):
    min_loss = float('inf')
    buy_year = sell_year = -1
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] < prices[i]:  # loss only
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1
                    sell_year = j + 1

    return buy_year, sell_year, min_loss

# Example usage:
prices = [20, 15, 7, 2, 13]
buy, sell, loss = minimize_loss(prices)
print(f"Buy in year {buy}, Sell in year {sell}, Loss = {loss}")
