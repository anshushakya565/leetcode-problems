class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = str(x)
        if org == org[::-1]:
            return True
        else:
            return False