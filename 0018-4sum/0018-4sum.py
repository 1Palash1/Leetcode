class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        s=set()
        output=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l=len(nums)-1
                while k<l:
                    sum1=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum1==target:
                        s.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif sum1<target:
                        k+=1
                    else:
                        l-=1
        return list(s)