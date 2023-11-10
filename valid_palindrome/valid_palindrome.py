import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        replaced_symbols = [r"[_-;,.\s]\s*"]
        for i in replaced_symbols:
            string_to_replace = s.replace(i, '')
            string_to_split = re.split(r"[\b\W\b_]+", string_to_replace)
            vowels_str = "".join(string_to_split)
            a = vowels_str.lower()
            reversed_a = a[::-1]
        if a == reversed_a:
            return True
        else:
            return False


a = Solution()
a.isPalindrome(s="ab_a")











