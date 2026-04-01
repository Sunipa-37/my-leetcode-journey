class Solution(object):
    def majorityElement(self, nums):
        freq = {}

        # Count frequency
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Find element with maximum frequency
        n= None
        max_value = 0

        for key in freq:
            if freq[key] > max_value:
                max_value = freq[key]
                n = key

        return n
