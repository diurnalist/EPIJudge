from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    first_trade_profits = [0.0]*len(prices)
    first_trade_min = float('inf')
    first_trade_max_profit = 0.0
    for i in range(len(prices)):
        first_trade_min = min(first_trade_min, prices[i])
        first_trade_max_profit = max(first_trade_max_profit, prices[i] - first_trade_min)
        first_trade_profits[i] = first_trade_max_profit

    second_trade_profits = [0.0]*len(prices)
    second_trade_max = float('-inf')
    second_trade_max_profit = 0.0
    for i in reversed(range(len(prices))):
        second_trade_max = max(second_trade_max, prices[i])
        second_trade_max_profit = max(second_trade_max_profit, second_trade_max - prices[i])
        second_trade_profits[i] = second_trade_max_profit

    max_total_profit = 0.0
    for i in range(len(prices)):
        max_total_profit = max(max_total_profit, first_trade_profits[i] + second_trade_profits[i])
    return max_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
