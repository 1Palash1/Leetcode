class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def mergeSort(arr):
            if len(arr)<=1:
                return 0
            mid=len(arr)//2
            left=arr[:mid]
            right=arr[mid:]

            count=mergeSort(left)
            count+=mergeSort(right)
            j=0
            for i in range(len(left)):
                while j<len(right) and left[i]>2*right[j]:
                    j+=1
                count+=j
            i=0
            j=0
            temp=[]
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    temp.append(left[i])
                    i+=1
                else:
                    temp.append(right[j])
                    j+=1
            while i<len(left):
                temp.append(left[i])
                i+=1
            while j<len(right):
                temp.append(right[j])
                j+=1
            arr[:]=temp
            return count
        return mergeSort(nums)