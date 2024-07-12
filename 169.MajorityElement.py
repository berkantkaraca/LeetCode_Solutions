#Problem
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# Follow-up: Could you solve the problem in linear time and in O(1) space?

#Solution 1 => Time Complexity: O(n^2), Space Complexity: O(n)
def majorityElement(nums):
    hashSet = set(nums)
    hashList = list(hashSet)

    counter = 0 
    result = 0
    flag = 0

    for i in range(0,len(hashList)):
        for j in range(0,len(nums)):
            if hashList[i] == nums[j]:
                counter += 1
        if counter > result:
            result = counter
            flag = hashList[i]
        counter = 0 
    return flag

#Solution 2 => Time Complexity: O(n), Space Complexity: O(n)
def majorityElement2(nums):
    numbers = {} #hashmap oluşturdu (dictionary)
    result = 0
    maxNumber = 0
    for num in nums:
        numbers[num] = 1 + numbers.get(num,0)
        if numbers[num] > maxNumber:
            result = num
        maxNumber = max(maxNumber, numbers[num])
    return result

#Solution 3 => Time Complexity: O(n), Space Complexity: O(1)
#Boyer Moore
def majorityElement3(nums):
    result = 0
    counter = 0

    for num in nums:
        if counter == 0:
            result = num

        # if result == num:
        #     counter += 1
        # else:
        #     counter -= 1
        counter += 1 if result == num else -1
   
    return result   

nums = [3,11,11,11,11,2,2,3,4,4,4,4,4,4]
print(majorityElement(nums))  #print 4
print(majorityElement2(nums)) #print 4
print(majorityElement3(nums)) #print 4