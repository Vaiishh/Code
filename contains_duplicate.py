class Solution(object):
    def containsDuplicate(self, nums):
        found=set()
        for i in nums:
            if i in found:
                return True
            found.add(i)
        return False         
        