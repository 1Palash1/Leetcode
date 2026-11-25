class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def helper(divisor):
            result=sum((n+divisor-1)//divisor for n in nums)
            if result>threshold:
                return False
            return True
        left,right=1,max(nums)
        while left<right:
            mid=(left+right)//2
            if helper(mid):
                right=mid
            else:
                left=mid+1
        return left