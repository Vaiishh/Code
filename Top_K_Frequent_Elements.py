from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        a={}
        result=[]
        a=Counter(nums)
        for i in range(0,k):
            key = (max(a, key=a.get))
            result.append(key)
            del a[key]
        return result    
       
        
