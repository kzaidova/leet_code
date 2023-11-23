class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_1_sps = ""
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i == len(word1):
                word_1_sps +=word2[j]
                j = j + 1
                continue
            if j == len(word2):
                word_1_sps +=word1[i]
                i = i + 1
                continue
            word_1_sps+=word1[i]
            word_1_sps+=word2[j]
            i = i + 1
            j = j + 1
        return str(word_1_sps)


a = Solution()
a.mergeAlternately(word1 = "abc", word2 = "pqrsssss")
