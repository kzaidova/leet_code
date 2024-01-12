class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        elements = ['a','e','i','o','u', 'A','E','I','O','U']
        res = ""
        for i in range(0, len(s)):
            if s[i] in elements:
                vowels += s[i]
        for i in range(0, len(s)):
            if s[i] in elements:
                res+=vowels.pop()
            else:
                res+=s[i]
        print(res)











a = Solution()
a.reverseVowels(s = "aA")


