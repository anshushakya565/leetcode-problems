class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        t = 0
        for i in nums:
            t += i
        ls = 0
        for i in range(len(nums)):
            rs = t - ls - nums[i]
            if ls == rs:
                return i
            ls += nums[i]
        return -1