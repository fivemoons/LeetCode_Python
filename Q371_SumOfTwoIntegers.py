class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        for _ in range(32):
            a, b = a^b, (a&b) << 1
        return a % 4294967296 if a <= -4294967296 else a

if __name__ == '__main__':
    s1 = Solution()
    print s1.getSum(-12, -8)
