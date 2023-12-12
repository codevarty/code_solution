""" sellStock.py Leetcode problem: [121] https://leetcode.com/problems/best-time-to-buy-and-sell-stock """
from typing import List
import sys
import time

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        m_value = sys.maxsize
        for price in prices:
            m_value = min(m_value, price)
            # result 가 0이기 때문에 없는 경우는 0이 된다.
            result = max(result, price - m_value)
        return result


if __name__ == '__main__':
    sol = Solution()
    input_prices =[7,1,5,3,6,4]
    start = time.time()
    output = sol.maxProfit(input_prices)
    end = time.time()
    print(output)
    print(f"{end-start:.5f}second")
