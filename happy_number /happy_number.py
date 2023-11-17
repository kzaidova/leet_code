class Solution:
    def isHappy(self, n: int) -> bool:
        a = set()
        while True:
            tmp = []
            sums = 0
            if n==1:
                print(True)
                return True

            while n > 0:
                b = n % 10
                tmp.append(b)
                n = n // 10
            print(tmp)
            for i in tmp:
                sums = i * i + sums

            if sums == 1:
                print(True)
                return True

            if sums in a:
                print(False)
                return False

            a.add(sums)
            n = sums

a = Solution()
a.isHappy(n = 2)
