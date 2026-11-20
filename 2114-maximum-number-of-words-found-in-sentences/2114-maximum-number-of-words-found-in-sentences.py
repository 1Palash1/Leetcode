class Solution(object):
    def mostWordsFound(self, sentences):
        counter=0
        for i in sentences:
            temp=i.count(" ")
            counter=max(counter,temp)
        return counter+1