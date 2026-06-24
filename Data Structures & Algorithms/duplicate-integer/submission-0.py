class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False

        nums.sort()

        for i in range(1,len(nums)):
            
            if nums[i-1] == nums[i]:
                dup = True

        return dup
