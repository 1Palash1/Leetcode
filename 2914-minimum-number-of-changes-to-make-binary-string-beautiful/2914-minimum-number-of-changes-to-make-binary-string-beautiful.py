class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        changes=0
        for i in range(0,n,2):
            if s[i]!=s[i+1]:
                changes+=1
        return changes