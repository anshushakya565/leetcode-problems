class Solution:
    def reverse(self, x: int) -> int:
        org = x
        if x < 0:
            x = x * -1
        rev = 0
        while (x != 0):
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        if rev not in range(-2 ** 31, 2 ** 31 - 1):
            return 0
        if org < 0:
            return rev * -1
        else:
            return rev
        
        

        