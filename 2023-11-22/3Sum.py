""" 3Sum.py Leetcode problem: [15] https://leetcode.com/problems/3sum """
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer solution => O(n2)
        # 투 포인터를 이용해서 풀어보자.
        lst = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) -1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    lst.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right -1]:
                        left -=1
                    left +=1
                    right-=1
        return lst


if __name__ == '__main__':
    sol = Solution()
    input_nums = [-1, 0, 1, 2, -1, -4]
    output = sol.threeSum(nums=input_nums)
    print(output)
