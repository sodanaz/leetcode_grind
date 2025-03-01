def searchInsert(nums, target):
    start_index = 0
    end_index = len(nums) - 1 # working with indices
    while start_index <= end_index:
        
        mid_index = (start_index + end_index)//2
        
        if target == nums[mid_index]:
            return mid_index
        elif target < nums[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    
    
    return start_index
    

list1 = [1,2,4,5,6,7]
print(searchInsert(list1, 3))


    