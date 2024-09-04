# Best Time to Buy and Sell Stock


def answer(prices: list[int]):
    maxProfit = 0
    buy, sell = 0, 1

    while sell < len(prices):

        curProfit = prices[sell] - prices[buy]
        if curProfit < 0:
            buy = sell
        maxProfit = max(maxProfit, curProfit)
        sell += 1

    return maxProfit


if __name__ == "__main__":
    prices = [7, 1, 2, 6]
    print(answer(prices))
