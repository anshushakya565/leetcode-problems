class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        n = len(nums)
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1
        return False