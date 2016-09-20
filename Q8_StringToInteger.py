class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str is None or str == '':
            return 0
        
        flag = True
        if str[0] == '+':
            flag = True
            str = str[1:]
        elif str[0] == '-':
            flag = False
            str = str[1:]

        ans = 0
        for x in str:
            if x >= '0' and x <= '9':
                ans = ans * 10 + int(x)
            else:
                break
        if not flag:
            ans = -ans
        ans = max(ans, -2147483648)
        ans = min(ans,  2147483647)
        return ans

if __name__ == '__main__':
    s1 = Solution()
    print s1.myAtoi('-123x123')