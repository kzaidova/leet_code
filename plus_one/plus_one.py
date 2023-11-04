from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = 0
        for i in range(len(digits)-1, -1, -1):
            a = digits[i] + 1
            b = a // 10
            digits[i] = a % 10
            if a < 10:
                break
        if b >= 1:
            digits.insert(0, b)
            print(digits)
        return digits

a = Solution()
a.plusOne(digits = [9, 9])

