class Solution(object):
    def isPalindrome(self, s):
        import re
        s=re.sub(r'[^a-zA-Z]','', s).lower()
        if s==s[::-1]:
            return True
        return False                

