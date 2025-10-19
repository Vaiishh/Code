class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        digits = int(''.join(map(str, digits)))+1
        result = [int(d) for d in str(digits)]
        return result 



