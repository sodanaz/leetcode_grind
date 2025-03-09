
"""
The code below I wrote before actually looking at the solution code.
Just by the verbal instructions of a tutor.
"""

class Solution:
    def removeDuplicates(self, nums):
        i, j = 1, 1 # both pointers means indices
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
            else: 
                if i==j:
                    i +=1
                    j +=1
                else: 
                    nums[j] = nums[i]
                    j+=1
                    i+=1
        return j
    
"""
Now the code from youtube tutorial
"""

class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j