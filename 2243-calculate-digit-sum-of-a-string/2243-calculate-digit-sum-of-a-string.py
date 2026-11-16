class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans=s[:]
        while(len(ans)>k):
            cuts=[]
            for i in range(0,len(ans),k):
                appender=sum(int(x) for x in ans[i:i+k])
                cuts.append(str(appender))
            concat=""
            for i in cuts:
                concat+=i
            ans=concat
        return ans