from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums_2 = len(nums) + 1
        for i in range(0, len_nums_2):
            if i not in nums:
                return i

a = Solution()
a.missingNumber(nums = [9,6,4,2,3,5,7,0,1])