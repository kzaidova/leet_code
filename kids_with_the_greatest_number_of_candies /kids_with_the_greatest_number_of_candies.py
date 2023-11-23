from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        old_maximum = 0
        new_candies = []
        new_maximum = []
        for i in range(0, len(candies)):
            if candies[i] >= old_maximum:
                old_maximum = candies[i]
        for i in range(0, len(candies)):
            new_candies.append(candies[i] + extraCandies)
            if new_candies[i]>= old_maximum:
                new_maximum.append(True)
            else:
                new_maximum.append(False)



a = Solution()
a.kidsWithCandies(candies = [12,1,12], extraCandies = 10)