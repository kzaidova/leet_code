from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] = dict[nums[i]] + 1
        max = 0
        res = 0
        for x, y in dict.items():
            if y > max:
                max = y
                res = x
        return res



a = Solution()
a.majorityElement(nums = [6,5,5])