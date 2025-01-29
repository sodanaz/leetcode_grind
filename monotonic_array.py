class Solution:
    def isMonotonic(self, nums) -> bool:
        
        is_monotonic_incr = False
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0 or nums[i] - nums[i-1] == 0:
                is_monotonic_incr = True
            else:
                is_monotonic_incr = False
                break
        
        is_monotonic_decr = False
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] < 0 or nums[i] - nums[i-1] == 0:
                is_monotonic_decr = True
            else:
                is_monotonic_decr = False
                break
        if len(nums) == 1:
            return True
        else:
            return is_monotonic_decr or is_monotonic_incr