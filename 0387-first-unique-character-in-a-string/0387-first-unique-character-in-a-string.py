class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for key, value in dic.items():
            if value == 1:
                return s.index(key)
        return -1