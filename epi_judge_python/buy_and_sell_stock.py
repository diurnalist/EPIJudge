from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_so_far = float('inf')
    profit = 0.0
    for i in range(len(prices)):
        min_so_far = min(min_so_far, prices[i])
        profit = max(prices[i] - min_so_far, profit)
    return profit



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
