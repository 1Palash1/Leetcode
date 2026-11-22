class Solution(object):
    def countGoodNumbers(self, n):
        m=10**9+7
        even=((n-1)//2)+1
        odd=n-even
        return pow(5,even,m)*pow(4,odd,m)%m