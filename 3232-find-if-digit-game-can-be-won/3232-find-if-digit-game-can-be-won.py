class Solution(object):
    def canAliceWin(self, nums):
        al=[]
        bob=[]
        for i in nums:
            if i>9:
                al.append(i)
            else:
                bob.append(i)
        return sum(al)!=sum(bob)