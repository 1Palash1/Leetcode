class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freqMax=0
        cursum=0
        nums.sort()
        left=0
        for right in range(len(nums)):
            cursum+=nums[right]
            while cursum+k<nums[right]*(right-left+1):
                cursum-=nums[left]
                left+=1
            freqMax=max(freqMax,right-left+1)
        return freqMax