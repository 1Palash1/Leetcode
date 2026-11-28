class Solution(object):
    def combinationSum2(self, candidates, target):
        res=[]
        combi=[]
        candidates.sort()

        def bkt(target, index):
            if target==0:
                res.append(combi[:])
                return
            if index==len(candidates) or target<0:
                return

            nextIndex=index+1
            while nextIndex<len(candidates) and candidates[index]==candidates[nextIndex]:
                nextIndex+=1

            bkt(target,nextIndex)
            combi.append(candidates[index])
            bkt(target-candidates[index],index+1)
            combi.pop()

        bkt(target,0)
        return res