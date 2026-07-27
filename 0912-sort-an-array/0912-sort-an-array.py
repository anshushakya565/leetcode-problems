class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            m = len(nums) // 2
            lo = self.sortArray(nums[:m])
            hi = self.sortArray(nums[m:])
            i, j, k = 0, 0, 0

            while i < len(lo) and j < len(hi):
                if lo[i] <= hi[j]:
                    nums[k] = lo[i]
                    i += 1
                else:
                    nums[k] = hi[j]
                    j += 1
                k += 1
            while i < len(lo):
                nums[k] = lo[i]
                i += 1
                k += 1
            while j < len(hi):
                nums[k] = hi[j]
                j += 1
                k += 1

        return nums