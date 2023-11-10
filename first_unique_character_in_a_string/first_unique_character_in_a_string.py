
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            unique = True
            for j in range(0, len(s)):
                if s[i] == s[j] and i != j:
                    unique = False
                    break
            if unique == True:
                print(i)
                return i
        print(-1)
        return -1



o = Solution()
o.firstUniqChar(s = "aabb")

