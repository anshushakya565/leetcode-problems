class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        res1 = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                res1 = mid
                hi = mid - 1
            elif nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid -1
        lo = 0
        hi = len(nums) - 1
        res2 = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                res2 = mid
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return res1, res2