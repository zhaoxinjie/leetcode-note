class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(1, l ):
            for j in range(i+1, l +1):
                if nums[-j] < nums[-i]:
                    nums[-j],nums[-i] = nums[-i], nums[-j]

                    return
        return


Solution().nextPermutation([1,3,2])

"""
def nextPermutation(self, nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return 
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1
"""