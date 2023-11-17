class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = []
        alfabet = 26
        a = 65
        full_alfabet = {}
        columnNumber = 0
        for i in range (0, len(columnTitle)):
            column.append(columnTitle[i])

        for i in range(1, alfabet + 1):
            full_alfabet[chr(a)] = i
            a = a + 1

        for i in range(len(column)-1, -1, -1):
            k = 1
            for j in range(i, len(columnTitle)-1):
                k = k * alfabet
            columnNumber += full_alfabet.get(column[i]) * k
        return columnNumber

a = Solution()
a.titleToNumber(columnTitle = "XXX")

