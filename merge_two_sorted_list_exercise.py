class Solution:
    def reverseString(self, s: list[str]) -> None:
        n = len(s)
        k = len(s) // 2
        for i in range(0, k):
            a = s[i]
            j = n-i-1
            s[i] = s[j]
            s[j] = a
        print(s)
        return s


