""" partition.py Leetcode problem: [561] https://leetcode.com/problems/array-partition """
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort를 한 후 0, 2, 4 .. 2*n 인덱스를 더하면 된다.
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    sol = Solution()
    input_nums = [1, 1, 1, 1, 1, 1]
    output = sol.arrayPairSum(input_nums)
    print(output)
