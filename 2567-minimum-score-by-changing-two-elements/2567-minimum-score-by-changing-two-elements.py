class Solution(object):
    def minimizeSum(self, nums):
        if len(nums)<4:
            return 0
        nums.sort()
        maxScore=nums[len(nums)-3]-nums[0]
        minScore=nums[len(nums)-1]-nums[2]
        maxMin=nums[len(nums)-2]-nums[1]
        return min(maxScore,minScore,maxMin)