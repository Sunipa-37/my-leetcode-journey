class Solution(object):
    def removeDuplicates(self, nums):
        n = []
        for i in nums:
            if i not in n:
                n.append(i)
        k = len(n)      
        nums[:] = n
        return k
