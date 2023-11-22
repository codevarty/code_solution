""" trappingRain.py Leetcode problem: [42] https://leetcode.com/problems/trapping-rain-water """
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # stack solution
        stack = []
        result = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:

                top = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                result += (distance * water)
            stack.append(i)
        return result


if __name__ == '__main__':
    sol = Solution()
    h = [4, 2, 0, 3, 2, 5]
    output = sol.trap(h)
    print(output)
