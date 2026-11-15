class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD= 10**9 + 7
        even,odd,parity,ans=1,0,0,0
        for i in arr:
            parity^=(i&1)
            if parity==1:
                ans=(ans+even)%MOD
                odd+=1
            else:
                ans=(ans+odd)%MOD
                even+=1
        return ans