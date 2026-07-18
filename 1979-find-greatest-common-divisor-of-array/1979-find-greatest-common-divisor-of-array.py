import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while b != 0:
            rem = a % b
            a = b
            b = rem
        return a
        