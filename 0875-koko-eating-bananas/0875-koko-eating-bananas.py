class Solution(object):
    def minEatingSpeed(self, piles, h):
        def helper(divisor):
            result=sum((n+divisor-1)//divisor for n in piles)
            if result>h:
                return False
            return True
        left,right=1,max(piles)
        while left<right:
            mid=(left+right)//2
            if helper(mid):
                right=mid
            else:
                left=mid+1
        return left