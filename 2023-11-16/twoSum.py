""" twoSum.py Leetcode problem: [1] https://leetcode.com/problems/two-sum/ """
from typing import List, Any


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2023-11-20 문제 재 풀이
        # 딕셔너리 같은 경우 해쉬 테이블이므로 키를 찾는 속도가 O(1)으로 빠르다.
        nums_dict = {}
        for i, num in enumerate(nums):
            # 인덱스와 값을 반대로 키와 값으로 저장한다.
            nums_dict[num] = i
        for i, num in enumerate(nums):
            if target - num in nums_dict and i != nums_dict[target - num]:
                return [i, nums_dict[target-num]]


"""test case"""
if __name__ == '__main__':
    solution = Solution()
    test_list = [3,2,4]
    test_target = 6
    result = solution.twoSum(test_list, test_target)
    print(result)
