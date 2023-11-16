class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        spisok_s = {}
        spisok_t = {}

        for i in range(0, len_s):
            if s[i] not in spisok_s:
                spisok_s[s[i]] = 1
            else:
                spisok_s[s[i]] = spisok_s[s[i]] + 1
        for i in range(0, len_t):
            if t[i] not in spisok_t:
                spisok_t[t[i]] = 1
            else:
                spisok_t[t[i]] = spisok_t[t[i]] + 1

        if len_s != len_t:
            return False

        for k, v in spisok_s.items():
            if k not in spisok_t.keys():
                return False
            else:
                if spisok_t.get(k) != v:
                    return False
        return True


a = Solution()
a.isAnagram(s = "rat", t = "car")