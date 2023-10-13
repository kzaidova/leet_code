class Solution:
    def reverseString(self, s: list[str]) -> None:
        len_s = len(s)
        len_s_sep_on_2 = len(s) // 2
        for i in range(0, len_s_sep_on_2):
            a = s[i]
            symmetric = len_s-i-1
            s[i] = s[symmetric]
            s[symmetric] = a
        print(s)
        return s


