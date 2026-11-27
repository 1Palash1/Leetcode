class Solution(object):
    def canPartition(self, arr, maxSum, maxParti):
        partition=1
        curSum=0
        for a in arr:
            if a>maxSum:
                return False
            if a+curSum<=maxSum:
                curSum+=a
            else:
                partition+=1
                curSum=a
                if partition>maxParti:
                    return False
        return partition<=maxParti

    def splitArray(self, nums, k):
        totalSum=0
        maxEl=0
        for i in nums:
            maxEl=max(maxEl,i)
            totalSum+=i
        l,r=maxEl,totalSum
        while l<r:
            mid=l+(r-l)//2
            if self.canPartition(nums,mid,k):
                r=mid
            else:
                l=mid+1
        return l