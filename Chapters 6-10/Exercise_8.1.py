#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, 
# and returns None. Then write a function called middle that takes a list and returns a new list that contains 
# all but the first and last elements.

def chop(nums):
    del nums[0]
    del nums[len(nums)-1]
    return None

def middle(nums):
    return chop(nums)

nums = [3, 41, 12, 9, 74, 15, 2, 3, 4, 5]
middle(nums)
print(nums)