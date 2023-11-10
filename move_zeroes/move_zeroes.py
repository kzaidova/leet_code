from typing import List

class Solution_1:
    def moveZeroes_1(self, nums: List[int]) -> None:
        for i in range(0, len(nums)):
            while nums[i] == 0:
                a = nums[i]
                nums.append(a)
                nums.remove(nums[i])
                break
        print(nums)
        return
s = Solution_1()
s.moveZeroes_1(nums = [0,0,1])

