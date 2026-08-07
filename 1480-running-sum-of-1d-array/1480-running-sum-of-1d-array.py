class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        li = []
        for i in nums:
            sum += i
            li.append(sum)
        return li