class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short_str = ""
        curr_prefix = ""
        comm_prefix = ""

        if len(str2)<len(str1):
            short_str=str2
        else:
            short_str=str1

        for i in short_str:
            curr_prefix += i
            n = len(str1) // len(curr_prefix)
            m =len(str2) // len(curr_prefix)
            curr_prefix_1 = curr_prefix * n
            curr_prefix_2 = curr_prefix * m
            if curr_prefix_1 == str1 and curr_prefix_2 == str2:
                comm_prefix = curr_prefix
        return comm_prefix

a = Solution()
a.gcdOfStrings(str1 = "ABCACB", str2 = "AB")