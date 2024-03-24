def twoSum(nums: list[int], target: int) -> list[int]:
    found = False
    count = 0
    
    # checkeo hasta len(nums)-2 porque el ultimo elemento solo no puede ser solución
    while ((count<=(len(nums)-2)) & (not found)):
        i = count+1

        limitI = (i<=(len(nums)-1))
        hitTarget = (nums[count]+nums[i] == target)
       
        while ((limitI) & (not hitTarget)):
            i += 1
          
            limitI = (i<(len(nums)-1))
            hitTarget = (nums[count]+nums[i] == target)
 
        if hitTarget:
            found = True
        else:
            count += 1
    
    return [count, i]
                

nums1 = [40,7,11,2]
tar1 = 9
nums2 = [3,2,4]
tar2 = 6
nums3 = [3,3]
tar3 = 6
twoSum1 = twoSum(nums1, tar1)
twoSum2 = twoSum(nums2, tar2)
twoSum3 = twoSum(nums3, tar3)
print(twoSum1)
print(twoSum2)
print(twoSum3)
#------------------------------------------------------- 
# DESCRIPTION: (difficulty=EASY)
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
