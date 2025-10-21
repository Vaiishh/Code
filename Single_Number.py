class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = 0
        for num in nums:
            final ^= num
        return final  