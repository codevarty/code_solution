""" twoSum.py Leetcode problem: [1] https://leetcode.com/problems/two-sum/ """
from typing import List, Any


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 인덱스 리스트를 반환한다.
        index_lst = []

        # taget이 nums의 요소 두개의 합 이 것이 중요하다.
        # 가장 최악의 방법이 이중 for문을 이용해서 하는 것이다. o(n + nlog(n))
        # 힌트 : 배열을 변경할 수 있지 않을까?? 이 부분이 마음에 걸리네
        for i in range(len(nums)):
            num_a = nums[i]
            target_temp = target - num_a
            try:
                t = nums.index(target_temp, i+1)
            except ValueError:
                t = -1
            if t != -1:
                index_lst.append(i)
                index_lst.append(t)

        return index_lst


"""test case"""
if __name__ == '__main__':
    solution = Solution()
    test_list = [3, 2, 4]
    test_target = 6
    result = solution.twoSum(test_list, test_target)
    print(result)
