#Solution 1 => Time Complexity: O(n^2), Space Complexity: O(1)
def hasDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j] :
                return True
    return False

#Solution 2 => Time Complexity: O(n), Space Complexity: O(n)
def hasDuplicate2(nums):
    # hashset = set()
    # for num in nums:
    #     if num in hashset:
    #         return True
    #     else:
    #         hashset.add(num)
    # return False
    
    return len(nums) != len(set(nums))

#Solution 3 => Time Complexity: O(n logn), Space Complexity: O(1)
def hasDuplicate3(nums):
    nums = sorted(nums)

    for i in range(len(nums)-1):
        if ((nums[i] == (nums[i+1]))):
            return True
    return False    
    
nums = [1,2,3,4]
print(hasDuplicate(nums)) #return False
print(hasDuplicate2(nums)) #return False
print(hasDuplicate3(nums)) #return False

nums = [1,2,3,4,2]
print(hasDuplicate(nums)) #return True
print(hasDuplicate2(nums)) #return True
print(hasDuplicate3(nums)) #return True