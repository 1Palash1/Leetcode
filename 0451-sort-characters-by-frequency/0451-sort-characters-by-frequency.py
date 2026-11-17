class Solution(object):
    def frequencySort(self, s):
        dict1={}
        ans=""
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in sorted(dict1, key=lambda x: dict1[x], reverse=True):
            ans+=i*(dict1.get(i))
        return ans