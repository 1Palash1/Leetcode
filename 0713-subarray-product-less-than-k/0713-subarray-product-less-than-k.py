class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        n=len(nums)
        if k<=1:
            return 0
        i=0
        j=0
        count=0
        prod=1
        while j<n:
            prod*=nums[j]
            while prod>=k:
                prod/=nums[i]
                i+=1
            count+=j-i+1
            j+=1
        return count