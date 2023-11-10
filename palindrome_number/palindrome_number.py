
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = []
        while x>0:
            b = x % 10
            tmp.append(b)
            x = x // 10
        i = 0
        j = len(tmp) - 1
        while i < len(tmp) / 2:
            if tmp[i] != tmp[j]:
                return False
            i = i + 1
            j =  j - 1
        return True
a = Solution()
a.isPalindrome(x = 12321)


class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        for i in range(0, len(str(x))):
            a = str(x)
            b = a[::-1]
            if a == b:
                return True
            else:
                return False

a = Solution_2()

a.isPalindrome(x = 12321)
