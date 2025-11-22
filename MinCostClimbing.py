class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n= len(cost)
        a,b=0,0
        for i in range (2, n+1):
            c=min(b+cost[i-1], a+cost[i-2])
            a,b=b,c
        return b    