""" exceptSelf.py Leetcode problem: [238] https://leetcode.com/problems/product-of-array-except-self """
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        p = 1
        for i in range(len(nums)):
            lst.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            lst[i] = lst[i] * p
            p = p * nums[i]
        return lst


if __name__ == '__main__':
    sol = Solution()
    input_nums = [-1, 1, 0, -3, 3]
    output = sol.productExceptSelf(input_nums)
    print(output)
