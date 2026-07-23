class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r <= len(nums) - 2:
            if nums[l] != nums[r]:
                return nums[l]
            l += 2
            r += 2
        return nums[-1]
