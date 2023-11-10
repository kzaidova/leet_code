from typing import List


##№1
def removeDuplicates():
     nums = [1,1,2]
     for i in range(0, len(nums)):
          j = i+1
          if i < len(nums):
               while j <len(nums) and nums[i] == nums[j]:
                    nums.pop(j)
     print(nums)
     return nums



##№2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i >= len(nums):
                 break

            j = i+1
            while j <len(nums) and nums[i] == nums[j]:
               nums.pop(j)
        return len(nums)