# Problem:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

#Solution 1 => Time Complexity: O(n^2), Space Complexity: O(1)
def singleNumber(nums):
    if(len(nums) == 1): return nums[0]
    else:
        for i in range(0,len(nums)):
            counter = 0
            for j in range(0,len(nums)):
                if i == j: 
                    continue
                if(nums[i] == nums[j]):
                    counter += 1
                i 
            if counter == 0: return nums[i]

#Solution 2 => Time Complexity: O(n), Space Complexity: O(1)
def singleNumber2(nums):
    result = 0
    for num in nums:
        result = result ^ num 
    return result

nums = [2,1,2,4,3,4,3,5,5]
print(singleNumber(nums))   #print 1
print(singleNumber2(nums))  #print 1