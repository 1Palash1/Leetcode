class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        ans=0
        s1=set(nums)
        nums1=list(s1)
        nums1.sort()
        curmax=1
        for i in range(1,len(nums1)):
            if(nums1[i]==nums1[i-1]+1):
                curmax+=1
            else:
                ans=max(ans,curmax)
                curmax=1
        ans=max(ans,curmax)
        return ans