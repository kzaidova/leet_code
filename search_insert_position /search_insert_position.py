from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        if target not in nums:
            while i < len(nums) and target > nums[i]:
                i = i+1
            else:
                nums.insert(i, target)
                return i
        else:
            for i in range(0, len(nums)):
                if target == nums[i]:
                    return i


a = Solution()
a.searchInsert(nums = [1,3,5,6], target = 7)