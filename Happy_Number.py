class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=set()
        while n != 1 and n not in a:
            a.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n==1    
