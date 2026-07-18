import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a, b = nums[-1], nums[0]
        while b != 0:
            rem = a % b
            a = b
            b = rem
        return a
        