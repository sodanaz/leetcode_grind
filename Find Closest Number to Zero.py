class Solution:
    def findClosestNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        neg_num = []
        pos_num = []

        for i in nums:
            if i < 0:
                neg_num.append(i)
            elif i > 0:
                pos_num.append(i)
            else:
                return i
        
        # Sort lists
        neg_num.sort(reverse=True)  # Largest negative number first
        pos_num.sort()  # Smallest positive number first

        # Handle edge cases where one of the lists might be empty
        if not neg_num:
            return pos_num[0]  # No negative numbers, return smallest positive
        if not pos_num:
            return neg_num[0]  # No positive numbers, return largest negative
        
        # Compare absolute values
        if abs(neg_num[0]) == pos_num[0]:
            return pos_num[0]  # Prefer positive in case of tie
        elif abs(neg_num[0]) > pos_num[0]:
            return pos_num[0]
        else:
            return neg_num[0]