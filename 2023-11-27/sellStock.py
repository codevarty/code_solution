""" sellStock.py Leetcode problem: [121] https://leetcode.com/problems/best-time-to-buy-and-sell-stock """
from typing import List
import sys
import time

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        m_value = sys.maxsize
        for i in range(len(prices)-1):
            m_value = min(m_value, prices[i])
            # result 가 0이기 때문에 없는 경우는 0이 된다.
            result = max(result, prices[i+1] - m_value)
        return result


if __name__ == '__main__':
    sol = Solution()
    input_prices = [2,4,1]
    start = time.time()
    output = sol.maxProfit(input_prices)
    end = time.time()
    print(output)
    print(f"{end-start:.5f}second")
